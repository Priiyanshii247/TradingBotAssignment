import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(
            args.quantity
        )

        if (
            args.type.upper()
            == "LIMIT"
            and
            args.price is None
        ):
            raise ValueError(
                "Price is required "
                "for LIMIT order"
            )

        print("\n========== ORDER REQUEST ==========")

        print(
            f"Symbol   : {args.symbol}"
        )

        print(
            f"Side     : {args.side}"
        )

        print(
            f"Type     : {args.type}"
        )

        print(
            f"Quantity : {args.quantity}"
        )

        if args.price:

            print(
                f"Price    : {args.price}"
            )

        response = place_order(
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print(
            "CLI file found!")
        

        print(
            f"Order ID     : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status       : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty : "
            f"{response.get('executedQty')}"
        )

        print(
            "\nSUCCESS"
        )

    except Exception as e:

        print(
            f"\nFAILED: {e}"
        )


if __name__ == "__main__":
    main()