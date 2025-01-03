import random

class Player:
    def __init__(self, name, tokens):
        self.name = name
        self.tokens = tokens
        self.total_score = 0
        self.lost_tokens = 0  # 잃은 토큰

    def borrow_tokens(self, amount):
        self.tokens += amount
        return True

    def lose_tokens(self, amount):
        self.tokens -= amount
        self.lost_tokens += amount


def get_user_input(player_name, round_number):
    while True:
        try:
            value = int(input(f"{player_name}님, {round_number}라운드의 주사위 값을 입력하세요 (1에서 6 사이의 정수): "))
            if 1 <= value <= 6:
                return value
            else:
                print("주사위 값은 1에서 6 사이의 정수여야 합니다.")
        except ValueError:
            print("정수를 입력해야 합니다.")


def main():
    while True:  # 게임을 계속해서 진행할지 여부를 묻는 무한 루프
        print("주사위 게임을 시작합니다!")
        num_players = int(input("참가할 플레이어 수를 입력하세요: "))

        players = []
        for i in range(num_players):
            name = input(f"{i+1}번 플레이어의 이름을 입력하세요: ")
            initial_tokens = 10000  # 각 플레이어에게 제공되는 초기 토큰 수
            players.append(Player(name, initial_tokens))

        rounds = int(input("몇 번 던지시겠습니까?: "))
        total_rounds = rounds * len(players)
        initial_rounds = 4  # 처음 4회 동안은 계속해서 돈을 딸 수 있도록 설정

        for round in range(rounds):
            print(f"\n라운드 {round+1}")

            # 각 플레이어의 베팅액 및 주사위 값 입력
            for player in players:
                print(f"\n{player.name}, 현재 토큰: {player.tokens}")
                bet_amount = int(input(f"{player.name}님, {round+1}라운드의 베팅할 금액을 입력하세요: "))
                while bet_amount > player.tokens:
                    print("보유한 토큰보다 높은 금액을 베팅할 수 없습니다.")
                    print("대출 시스템을 이용하여 부족한 토큰을 대출할 수 있습니다.")
                    choice = input("대출을 원하시면 'Y'를 입력하세요: ")
                    if choice.upper() == 'Y':
                        loan_amount = int(input("대출할 금액을 입력하세요: "))
                        if player.borrow_tokens(loan_amount):  # 대출 가능한 경우에만 대출받음
                            print(f"{player.name}님, {loan_amount} 토큰을 대출받았습니다.")
                            print(f"{player.name}님의 현재 토큰: {player.tokens}")
                            break
                    else:
                        bet_amount = int(input(f"{player.name}님, {round+1}라운드의 베팅할 금액을 입력하세요: "))

                player.bet_amount = bet_amount

                # 참가자가 입력한 주사위 값과 랜덤으로 나온 주사위 값이 일치하면 잭팟을 처리합니다.
                dice_value = get_user_input(player.name, round + 1)
                player.dice_value = dice_value

            # 주사위를 굴립니다.
            for player in players:
                print(f"\n{player.name}, 주사위를 굴리는 중...")
                dice_result = random.randint(1, 6)
                player.total_score += dice_result
                player.tokens -= player.bet_amount
                print(f"{player.name}의 결과: {dice_result}")

                # 잭팟을 처리합니다.
                if dice_result == player.dice_value:
                    print("잭팟!!! 베팅액의 5배를 받습니다!")
                    player.tokens += player.bet_amount * 6
                else:
                    player.tokens -= player.bet_amount * 1/2
                    print("아쉽게도 잭팟에는 당첨되지 않았습니다.")

        print("\n게임 종료!")
        print("\n최종 순위:")

        players.sort(key=lambda x: x.tokens, reverse=True)
        rank = 1
        for i, player in enumerate(players):
            print(f"{rank}위: {player.name} - 총점: {player.tokens}")
            rank += 1

        print("\n플레이어들의 현재 잔고 및 잃은 돈:")
        for player in players:
            print(f"{player.name}: 현재 잔고 - {player.tokens} 코인, 잃은 돈 - {player.lost_tokens} 코인")

        # 게임을 계속할 지 묻습니다.
        play_again = input("게임을 계속하시겠습니까? (Y/N): ")
        if play_again.upper() != 'Y':
            break  # 사용자가 'Y'를 입력하지 않으면 루프를 종료합니다.

if __name__ == "__main__":
    main()
