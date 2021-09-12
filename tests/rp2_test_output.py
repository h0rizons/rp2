# Copyright 2021 eprbell
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=C0302
RP2_TEST_OUTPUT = {
    "B1": """GainLossSet:
  configuration=./config/test_data.config
  asset=B1
  entries=
    GainLoss:
      id=2->None
      crypto_amount=2.00000000
      usd_cost_basis=0.0000
      usd_gain=24000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=24000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B1
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=None
    GainLoss:
      id=6->None
      crypto_amount=3.00000000
      usd_cost_basis=0.0000
      usd_gain=39000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=39000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=6
        timestamp=2020-03-01 09:45:00.000000 +0000
        asset=B1
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=13000.0000
        crypto_in=3.00000000
        usd_fee=0.0000
        usd_in_no_fee=39000.0000
        usd_in_with_fee=39000.0000
        is_taxable=True
        usd_taxable_amount=39000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=2->None""",
    "B2": """GainLossSet:
  configuration=./config/test_data.config
  asset=B2
  entries=
    GainLoss:
      id=15->3
      crypto_amount=0.20000000
      usd_cost_basis=2220.0000
      usd_gain=20.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=2240.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=OutTransaction:
        id=15
        timestamp=2020-01-11 11:15:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=11200.0000
        crypto_out_no_fee=0.20000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=2240.0000
      from_lot_usd_amount_with_fee_fraction=2220.0000
      from_lot_fraction_percentage=20.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=1 of 2
      parent=None
    GainLoss:
      id=2->None
      crypto_amount=2.00000000
      usd_cost_basis=0.0000
      usd_gain=24000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=24000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=15->3
    GainLoss:
      id=14->3
      crypto_amount=0.80000000
      usd_cost_basis=8880.0000
      usd_gain=880.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=9760.0000
      taxable_event_fraction_percentage=80.0000%
      taxable_event=OutTransaction:
        id=14
        timestamp=2020-02-11 19:58:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=12200.0000
        crypto_out_no_fee=1.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=12200.0000
      from_lot_usd_amount_with_fee_fraction=8880.0000
      from_lot_fraction_percentage=80.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 2
      from_lot_fraction=2 of 2
      parent=2->None
    GainLoss:
      id=14->2
      crypto_amount=0.20000000
      usd_cost_basis=2400.0000
      usd_gain=40.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=2440.0000
      taxable_event_fraction_percentage=20.0000%
      taxable_event=OutTransaction:
        id=14
        timestamp=2020-02-11 19:58:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=12200.0000
        crypto_out_no_fee=1.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=12200.0000
      from_lot_usd_amount_with_fee_fraction=2400.0000
      from_lot_fraction_percentage=10.0000%
      from_lot=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      taxable_event_fraction=2 of 2
      from_lot_fraction=1 of 2
      parent=14->3
    GainLoss:
      id=6->None
      crypto_amount=3.00000000
      usd_cost_basis=0.0000
      usd_gain=39000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=39000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=6
        timestamp=2020-03-01 09:45:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=13000.0000
        crypto_in=3.00000000
        usd_fee=0.0000
        usd_in_no_fee=39000.0000
        usd_in_with_fee=39000.0000
        is_taxable=True
        usd_taxable_amount=39000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=14->2
    GainLoss:
      id=16->2
      crypto_amount=1.80000000
      usd_cost_basis=21600.0000
      usd_gain=3960.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=25560.0000
      taxable_event_fraction_percentage=36.0000%
      taxable_event=OutTransaction:
        id=16
        timestamp=2020-04-11 07:10:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.GIFT
        spot_price=14200.0000
        crypto_out_no_fee=5.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=71000.0000
      from_lot_usd_amount_with_fee_fraction=21600.0000
      from_lot_fraction_percentage=90.0000%
      from_lot=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      taxable_event_fraction=1 of 3
      from_lot_fraction=2 of 2
      parent=6->None
    GainLoss:
      id=16->6
      crypto_amount=3.00000000
      usd_cost_basis=39000.0000
      usd_gain=3600.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=42600.0000
      taxable_event_fraction_percentage=60.0000%
      taxable_event=OutTransaction:
        id=16
        timestamp=2020-04-11 07:10:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.GIFT
        spot_price=14200.0000
        crypto_out_no_fee=5.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=71000.0000
      from_lot_usd_amount_with_fee_fraction=39000.0000
      from_lot_fraction_percentage=100.0000%
      from_lot=InTransaction:
        id=6
        timestamp=2020-03-01 09:45:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=13000.0000
        crypto_in=3.00000000
        usd_fee=0.0000
        usd_in_no_fee=39000.0000
        usd_in_with_fee=39000.0000
        is_taxable=True
        usd_taxable_amount=39000.0000
      taxable_event_fraction=2 of 3
      from_lot_fraction=1 of 1
      parent=16->2
    GainLoss:
      id=16->5
      crypto_amount=0.20000000
      usd_cost_basis=2820.0000
      usd_gain=20.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=2840.0000
      taxable_event_fraction_percentage=4.0000%
      taxable_event=OutTransaction:
        id=16
        timestamp=2020-04-11 07:10:00.000000 +0000
        asset=B2
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.GIFT
        spot_price=14200.0000
        crypto_out_no_fee=5.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=71000.0000
      from_lot_usd_amount_with_fee_fraction=2820.0000
      from_lot_fraction_percentage=5.0000%
      from_lot=InTransaction:
        id=5
        timestamp=2020-04-01 09:45:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=14000.0000
        crypto_in=4.00000000
        usd_fee=400.0000
        usd_in_no_fee=56000.0000
        usd_in_with_fee=56400.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=3 of 3
      from_lot_fraction=1 of 3
      parent=16->6
    GainLoss:
      id=12->5
      crypto_amount=3.79000000
      usd_cost_basis=53439.0000
      usd_gain=758.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=54197.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=OutTransaction:
        id=12
        timestamp=2020-04-12 17:50:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.DONATE
        spot_price=14300.0000
        crypto_out_no_fee=3.79000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=54197.0000
      from_lot_usd_amount_with_fee_fraction=53439.0000
      from_lot_fraction_percentage=94.7500%
      from_lot=InTransaction:
        id=5
        timestamp=2020-04-01 09:45:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=14000.0000
        crypto_in=4.00000000
        usd_fee=400.0000
        usd_in_no_fee=56000.0000
        usd_in_with_fee=56400.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=2 of 3
      parent=16->5
    GainLoss:
      id=13->5
      crypto_amount=0.01000000
      usd_cost_basis=141.0000
      usd_gain=61.0000
      is_long_term_capital_gains=True
      taxable_event_usd_amount_with_fee_fraction=202.0000
      taxable_event_fraction_percentage=0.4975%
      taxable_event=OutTransaction:
        id=13
        timestamp=2021-06-11 05:31:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=20200.0000
        crypto_out_no_fee=2.00000000
        crypto_fee=0.01000000
        is_taxable=True
        usd_taxable_amount=40602.0000
      from_lot_usd_amount_with_fee_fraction=141.0000
      from_lot_fraction_percentage=0.2500%
      from_lot=InTransaction:
        id=5
        timestamp=2020-04-01 09:45:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=14000.0000
        crypto_in=4.00000000
        usd_fee=400.0000
        usd_in_no_fee=56000.0000
        usd_in_with_fee=56400.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 2
      from_lot_fraction=3 of 3
      parent=12->5
    GainLoss:
      id=13->4
      crypto_amount=2.00000000
      usd_cost_basis=30200.0000
      usd_gain=10200.0000
      is_long_term_capital_gains=True
      taxable_event_usd_amount_with_fee_fraction=40400.0000
      taxable_event_fraction_percentage=99.5025%
      taxable_event=OutTransaction:
        id=13
        timestamp=2021-06-11 05:31:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=20200.0000
        crypto_out_no_fee=2.00000000
        crypto_fee=0.01000000
        is_taxable=True
        usd_taxable_amount=40602.0000
      from_lot_usd_amount_with_fee_fraction=30200.0000
      from_lot_fraction_percentage=40.0000%
      from_lot=InTransaction:
        id=4
        timestamp=2020-05-01 14:03:00.000000 +0000
        asset=B2
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=15000.0000
        crypto_in=5.00000000
        usd_fee=500.0000
        usd_in_no_fee=75000.0000
        usd_in_with_fee=75500.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=2 of 2
      from_lot_fraction=1 of 1
      parent=13->5""",
    "B3": """GainLossSet:
  configuration=./config/test_data.config
  asset=B3
  entries=
    GainLoss:
      id=25->3
      crypto_amount=0.01000000
      usd_cost_basis=111.0000
      usd_gain=3.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=114.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=IntraTransaction:
        id=25
        timestamp=2020-01-21 18:33:14.342000 +0000
        asset=B3
        from_exchange=Coinbase
        from_holder=Bob
        to_exchange=BlockFi
        to_holder=Bob
        transaction_type=TransactionType.MOVE
        spot_price=11400.0000
        crypto_sent=0.10000000
        crypto_received=0.09000000
        crypto_fee=0.01000000
        usd_fee=114.0000
        is_taxable=True
        usd_taxable_amount=114.0000
      from_lot_usd_amount_with_fee_fraction=111.0000
      from_lot_fraction_percentage=1.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B3
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=1 of 3
      parent=None
    GainLoss:
      id=2->None
      crypto_amount=2.00000000
      usd_cost_basis=0.0000
      usd_gain=24000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=24000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B3
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=25->3
    GainLoss:
      id=6->None
      crypto_amount=3.00000000
      usd_cost_basis=0.0000
      usd_gain=39000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=39000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=6
        timestamp=2020-03-01 09:45:00.000000 +0000
        asset=B3
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=13000.0000
        crypto_in=3.00000000
        usd_fee=0.0000
        usd_in_no_fee=39000.0000
        usd_in_with_fee=39000.0000
        is_taxable=True
        usd_taxable_amount=39000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=2->None
    GainLoss:
      id=24->3
      crypto_amount=0.02000000
      usd_cost_basis=222.0000
      usd_gain=66.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=288.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=IntraTransaction:
        id=24
        timestamp=2020-05-21 12:58:10.000000 +0000
        asset=B3
        from_exchange=Coinbase
        from_holder=Bob
        to_exchange=Kraken
        to_holder=Alice
        transaction_type=TransactionType.MOVE
        spot_price=14400.0000
        crypto_sent=0.20000000
        crypto_received=0.18000000
        crypto_fee=0.02000000
        usd_fee=288.0000
        is_taxable=True
        usd_taxable_amount=288.0000
      from_lot_usd_amount_with_fee_fraction=222.0000
      from_lot_fraction_percentage=2.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B3
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=2 of 3
      parent=6->None
    GainLoss:
      id=22->3
      crypto_amount=0.04000000
      usd_cost_basis=444.0000
      usd_gain=412.0000
      is_long_term_capital_gains=True
      taxable_event_usd_amount_with_fee_fraction=856.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=IntraTransaction:
        id=22
        timestamp=2021-07-21 10:02:02.000000 +0000
        asset=B3
        from_exchange=Coinbase
        from_holder=Bob
        to_exchange=Kraken
        to_holder=Alice
        transaction_type=TransactionType.MOVE
        spot_price=21400.0000
        crypto_sent=0.50000000
        crypto_received=0.46000000
        crypto_fee=0.04000000
        usd_fee=856.0000
        is_taxable=True
        usd_taxable_amount=856.0000
      from_lot_usd_amount_with_fee_fraction=444.0000
      from_lot_fraction_percentage=4.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B3
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=3 of 3
      parent=24->3""",
    "B4": """GainLossSet:
  configuration=./config/test_data.config
  asset=B4
  entries=
    GainLoss:
      id=15->3
      crypto_amount=0.20000000
      usd_cost_basis=2220.0000
      usd_gain=20.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=2240.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=OutTransaction:
        id=15
        timestamp=2020-01-11 11:15:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=11200.0000
        crypto_out_no_fee=0.20000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=2240.0000
      from_lot_usd_amount_with_fee_fraction=2220.0000
      from_lot_fraction_percentage=20.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=1 of 3
      parent=None
    GainLoss:
      id=25->3
      crypto_amount=0.01000000
      usd_cost_basis=111.0000
      usd_gain=3.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=114.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=IntraTransaction:
        id=25
        timestamp=2020-01-21 18:33:14.342000 +0000
        asset=B4
        from_exchange=Coinbase
        from_holder=Bob
        to_exchange=BlockFi
        to_holder=Bob
        transaction_type=TransactionType.MOVE
        spot_price=11400.0000
        crypto_sent=0.10000000
        crypto_received=0.09000000
        crypto_fee=0.01000000
        usd_fee=114.0000
        is_taxable=True
        usd_taxable_amount=114.0000
      from_lot_usd_amount_with_fee_fraction=111.0000
      from_lot_fraction_percentage=1.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=2 of 3
      parent=15->3
    GainLoss:
      id=2->None
      crypto_amount=2.00000000
      usd_cost_basis=0.0000
      usd_gain=24000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=24000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=25->3
    GainLoss:
      id=14->3
      crypto_amount=0.79000000
      usd_cost_basis=8769.0000
      usd_gain=869.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=9638.0000
      taxable_event_fraction_percentage=79.0000%
      taxable_event=OutTransaction:
        id=14
        timestamp=2020-02-11 19:58:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=12200.0000
        crypto_out_no_fee=1.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=12200.0000
      from_lot_usd_amount_with_fee_fraction=8769.0000
      from_lot_fraction_percentage=79.0000%
      from_lot=InTransaction:
        id=3
        timestamp=2020-01-01 08:41:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=11000.0000
        crypto_in=1.00000000
        usd_fee=100.0000
        usd_in_no_fee=11000.0000
        usd_in_with_fee=11100.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 2
      from_lot_fraction=3 of 3
      parent=2->None
    GainLoss:
      id=14->2
      crypto_amount=0.21000000
      usd_cost_basis=2520.0000
      usd_gain=42.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=2562.0000
      taxable_event_fraction_percentage=21.0000%
      taxable_event=OutTransaction:
        id=14
        timestamp=2020-02-11 19:58:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=12200.0000
        crypto_out_no_fee=1.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=12200.0000
      from_lot_usd_amount_with_fee_fraction=2520.0000
      from_lot_fraction_percentage=10.5000%
      from_lot=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      taxable_event_fraction=2 of 2
      from_lot_fraction=1 of 2
      parent=14->3
    GainLoss:
      id=6->None
      crypto_amount=3.00000000
      usd_cost_basis=0.0000
      usd_gain=39000.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=39000.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=InTransaction:
        id=6
        timestamp=2020-03-01 09:45:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=13000.0000
        crypto_in=3.00000000
        usd_fee=0.0000
        usd_in_no_fee=39000.0000
        usd_in_with_fee=39000.0000
        is_taxable=True
        usd_taxable_amount=39000.0000
      from_lot_usd_amount_with_fee_fraction=0.0000
      from_lot_fraction_percentage=0.0000%
      from_lot=None
      taxable_event_fraction=1 of 1
      parent=14->2
    GainLoss:
      id=16->2
      crypto_amount=1.79000000
      usd_cost_basis=21480.0000
      usd_gain=3938.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=25418.0000
      taxable_event_fraction_percentage=35.8000%
      taxable_event=OutTransaction:
        id=16
        timestamp=2020-04-11 07:10:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.GIFT
        spot_price=14200.0000
        crypto_out_no_fee=5.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=71000.0000
      from_lot_usd_amount_with_fee_fraction=21480.0000
      from_lot_fraction_percentage=89.5000%
      from_lot=InTransaction:
        id=2
        timestamp=2020-02-01 11:18:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=12000.0000
        crypto_in=2.00000000
        usd_fee=0.0000
        usd_in_no_fee=24000.0000
        usd_in_with_fee=24000.0000
        is_taxable=True
        usd_taxable_amount=24000.0000
      taxable_event_fraction=1 of 3
      from_lot_fraction=2 of 2
      parent=6->None
    GainLoss:
      id=16->6
      crypto_amount=3.00000000
      usd_cost_basis=39000.0000
      usd_gain=3600.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=42600.0000
      taxable_event_fraction_percentage=60.0000%
      taxable_event=OutTransaction:
        id=16
        timestamp=2020-04-11 07:10:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.GIFT
        spot_price=14200.0000
        crypto_out_no_fee=5.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=71000.0000
      from_lot_usd_amount_with_fee_fraction=39000.0000
      from_lot_fraction_percentage=100.0000%
      from_lot=InTransaction:
        id=6
        timestamp=2020-03-01 09:45:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.EARN
        spot_price=13000.0000
        crypto_in=3.00000000
        usd_fee=0.0000
        usd_in_no_fee=39000.0000
        usd_in_with_fee=39000.0000
        is_taxable=True
        usd_taxable_amount=39000.0000
      taxable_event_fraction=2 of 3
      from_lot_fraction=1 of 1
      parent=16->2
    GainLoss:
      id=16->5
      crypto_amount=0.21000000
      usd_cost_basis=2961.0000
      usd_gain=21.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=2982.0000
      taxable_event_fraction_percentage=4.2000%
      taxable_event=OutTransaction:
        id=16
        timestamp=2020-04-11 07:10:00.000000 +0000
        asset=B4
        exchange=BlockFi
        holder=Bob
        transaction_type=TransactionType.GIFT
        spot_price=14200.0000
        crypto_out_no_fee=5.00000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=71000.0000
      from_lot_usd_amount_with_fee_fraction=2961.0000
      from_lot_fraction_percentage=5.2500%
      from_lot=InTransaction:
        id=5
        timestamp=2020-04-01 09:45:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=14000.0000
        crypto_in=4.00000000
        usd_fee=400.0000
        usd_in_no_fee=56000.0000
        usd_in_with_fee=56400.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=3 of 3
      from_lot_fraction=1 of 2
      parent=16->6
    GainLoss:
      id=12->5
      crypto_amount=3.79000000
      usd_cost_basis=53439.0000
      usd_gain=758.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=54197.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=OutTransaction:
        id=12
        timestamp=2020-04-12 17:50:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.DONATE
        spot_price=14300.0000
        crypto_out_no_fee=3.79000000
        crypto_fee=0.00000000
        is_taxable=True
        usd_taxable_amount=54197.0000
      from_lot_usd_amount_with_fee_fraction=53439.0000
      from_lot_fraction_percentage=94.7500%
      from_lot=InTransaction:
        id=5
        timestamp=2020-04-01 09:45:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=14000.0000
        crypto_in=4.00000000
        usd_fee=400.0000
        usd_in_no_fee=56000.0000
        usd_in_with_fee=56400.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=2 of 2
      parent=16->5
    GainLoss:
      id=24->4
      crypto_amount=0.02000000
      usd_cost_basis=302.0000
      usd_gain=-14.0000
      is_long_term_capital_gains=False
      taxable_event_usd_amount_with_fee_fraction=288.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=IntraTransaction:
        id=24
        timestamp=2020-05-21 12:58:10.000000 +0000
        asset=B4
        from_exchange=Coinbase
        from_holder=Bob
        to_exchange=Kraken
        to_holder=Alice
        transaction_type=TransactionType.MOVE
        spot_price=14400.0000
        crypto_sent=0.20000000
        crypto_received=0.18000000
        crypto_fee=0.02000000
        usd_fee=288.0000
        is_taxable=True
        usd_taxable_amount=288.0000
      from_lot_usd_amount_with_fee_fraction=302.0000
      from_lot_fraction_percentage=0.4000%
      from_lot=InTransaction:
        id=4
        timestamp=2020-05-01 14:03:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=15000.0000
        crypto_in=5.00000000
        usd_fee=500.0000
        usd_in_no_fee=75000.0000
        usd_in_with_fee=75500.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=1 of 3
      parent=12->5
    GainLoss:
      id=13->4
      crypto_amount=2.01000000
      usd_cost_basis=30351.0000
      usd_gain=10251.0000
      is_long_term_capital_gains=True
      taxable_event_usd_amount_with_fee_fraction=40602.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=OutTransaction:
        id=13
        timestamp=2021-06-11 05:31:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.SELL
        spot_price=20200.0000
        crypto_out_no_fee=2.00000000
        crypto_fee=0.01000000
        is_taxable=True
        usd_taxable_amount=40602.0000
      from_lot_usd_amount_with_fee_fraction=30351.0000
      from_lot_fraction_percentage=40.2000%
      from_lot=InTransaction:
        id=4
        timestamp=2020-05-01 14:03:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=15000.0000
        crypto_in=5.00000000
        usd_fee=500.0000
        usd_in_no_fee=75000.0000
        usd_in_with_fee=75500.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=2 of 3
      parent=24->4
    GainLoss:
      id=22->4
      crypto_amount=0.04000000
      usd_cost_basis=604.0000
      usd_gain=252.0000
      is_long_term_capital_gains=True
      taxable_event_usd_amount_with_fee_fraction=856.0000
      taxable_event_fraction_percentage=100.0000%
      taxable_event=IntraTransaction:
        id=22
        timestamp=2021-07-21 10:02:02.000000 +0000
        asset=B4
        from_exchange=Coinbase
        from_holder=Bob
        to_exchange=Kraken
        to_holder=Alice
        transaction_type=TransactionType.MOVE
        spot_price=21400.0000
        crypto_sent=0.50000000
        crypto_received=0.46000000
        crypto_fee=0.04000000
        usd_fee=856.0000
        is_taxable=True
        usd_taxable_amount=856.0000
      from_lot_usd_amount_with_fee_fraction=604.0000
      from_lot_fraction_percentage=0.8000%
      from_lot=InTransaction:
        id=4
        timestamp=2020-05-01 14:03:00.000000 +0000
        asset=B4
        exchange=Coinbase
        holder=Bob
        transaction_type=TransactionType.BUY
        spot_price=15000.0000
        crypto_in=5.00000000
        usd_fee=500.0000
        usd_in_no_fee=75000.0000
        usd_in_with_fee=75500.0000
        is_taxable=False
        usd_taxable_amount=0.0000
      taxable_event_fraction=1 of 1
      from_lot_fraction=3 of 3
      parent=13->4""",
}
