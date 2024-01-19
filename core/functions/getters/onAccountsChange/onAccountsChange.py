import asyncio
from solana.rpc.api import Client
from solana.publickey import PublicKey

from .helpers import return_anchor_program, TRANSACTION_ACCOUNT_PARSERS

async def on_accounts_change(
    program_id: PublicKey,
    timeout_of_calls: int,
    from_this_signature: str,
    connection: Client,
    on_accounts_change_callback
):
    print('onAccountsChange')
    last_signature = from_this_signature or (await connection.get_signatures_for_address(
        program_id, {'limit': 1}, 'confirmed'))[0]['signature']
    
    while True:
        try:
            new_signature_infos = await connection.get_signatures_for_address(
                program_id, {'limit': 50, 'until': last_signature}, 'confirmed')

            if not new_signature_infos:
                await asyncio.sleep(0.2)
                continue

            if len(new_signature_infos) > 10:
                print('more than 10 signatures error: ', len(new_signature_infos))
                latest_confirmed_signatures = await connection.get_signatures_for_address(
                    program_id, {'limit': 1}, 'confirmed')
                if not latest_confirmed_signatures:
                    continue
                last_signature = latest_confirmed_signatures[0]['signature']
                await asyncio.sleep(0.2)
                continue

            for signature_info in reversed(new_signature_infos):
                await asyncio.sleep(0.1)
                current_transaction_info = await connection.get_parsed_transaction(
                    signature_info['signature'], 'confirmed')

                if not current_transaction_info:
                    last_signature = signature_info['signature']
                    await asyncio.sleep(0.1)
                    continue

                if not current_transaction_info['meta'] or current_transaction_info['meta']['err'] is not None:
                    last_signature = signature_info['signature']
                    await asyncio.sleep(0.1)
                    continue

                instruction_log = current_transaction_info['meta']['logMessages'][1]
                if instruction_log in TRANSACTION_ACCOUNT_PARSERS:
                    try:
                        await on_accounts_change_callback(
                            await TRANSACTION_ACCOUNT_PARSERS[instruction_log](
                                {'transaction': current_transaction_info, 'programId': program_id, 'connection': connection}
                            ),
                            instruction_log
                        )
                        last_signature = signature_info['signature']
                    except Exception as err:
                        last_signature = signature_info['signature']
                        print('onAccountsChange Error in', instruction_log, ':', err)
                        await asyncio.sleep(0.1)
                        continue
        except Exception as err:
            latest_confirmed_signatures = await connection.get_signatures_for_address(
                program_id, {'limit': 1}, 'confirmed')
            last_signature = latest_confirmed_signatures[0]['signature'] if latest_confirmed_signatures else None
            print('onAccountsChange Error:', err)

        await asyncio.sleep(timeout_of_calls or 5.0)
