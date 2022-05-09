
def battery_is_ok(temperature, soc, charge_rate):
    if(temperature_is_ok(temperature) and soc_is_ok(soc) and charge_rate_is_ok(charge_rate)):
        return True
    else:
        return False


def temperature_is_ok(temperature):
    if temperature < 0 or temperature > 45:
        print_text('Temperature is out of range!')
        return False
    else:
        return True


def soc_is_ok(soc):
    if soc < 20 or soc > 80:
        print_text('State of Charge is out of range!')
        return False
    else:
        return True


def charge_rate_is_ok(charge_rate):
    if charge_rate > 0.8:
        print_text('Charge rate is out of range!')
        return False
    else:
        return True


def print_text(text):
    print(text)


if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
