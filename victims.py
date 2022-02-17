def convert_victim_format(data: str) -> dict:
    names, card_data, pwd, ffa = data.split(';')
    name, surname = names.split(' ')
    card_no, card_exp, card_that_third_thing = card_data.split(',')
    return create_victim_dict(name, surname, int(card_no), card_exp, int(card_that_third_thing), pwd, ffa == 'f')


def create_victim_dict(name: str, surname: str, card_no: int, card_exp: str, card_that_third_thing: int, pwd: str,
                       ffa: bool) -> dict:
    return {
        "name": name,
        "surname": surname,
        "card_no": card_no,
        "card_exp": card_exp,
        "card_that_third_thing": card_that_third_thing,
        "pwd": pwd,
        "2factor": ffa
    }


if __name__ == '__main__':
    raw_data = [
        "Karel Vopěnka;1654731544681137,10/25,487;iamthecapitannow;t",
        "Ekaterina Pogonisheva;3685147993221530,12/22,369;<3pogoftw;f",
        "Jana Poláková;5168467833451129,02/19,498;lol;f"
    ]
    print('\n'.join(map(lambda d: '' + str(convert_victim_format(d)), raw_data)))
