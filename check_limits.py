import re

def battery_is_ok(temperature, soc, charge_rate):
    return (temperature_is_ok(temperature) and soc_is_ok(soc) and charge_rate_is_ok(charge_rate))


def temperature_is_ok(temperature):
    temperature_value = get_value_from_feature(temperature)
    return is_feature_in_limit(0, 45, temperature_value, 'Temperature')


def soc_is_ok(soc):
    return is_feature_in_limit(20, 80, soc, 'SOC')


def charge_rate_is_ok(charge_rate):
    return is_feature_in_limit(0, 0.8, charge_rate, 'Charge_Rate')

def get_value_from_feature(feature_value):
    return int(re.sub('[A-Za-z]',"", feature_value))


def get_unit_from_feature(feature_value):
    return re.sub('[0-9]',"", feature_value)


def check_lower_limit(lower_limit, upper_limit, feature_value):
    if((feature_value <= (lower_limit+(upper_limit*5)/100) and feature_value >= lower_limit)):
        print('Warning: Approaching discharge')
        print("Warnung: Naht Entladung")


def check_upper_limit(upper_limit, feature_value):
    if((feature_value >= (upper_limit-(upper_limit*5)/100) and feature_value <= upper_limit)):
        print('Warning: Approaching charge-peak')
        print("Warnung: Ladespitze nähert sich")


def is_feature_in_limit(lower_limit, upper_limit, feature_value, feature):
    check_lower_limit(lower_limit, upper_limit, feature_value)
    check_upper_limit(upper_limit, feature_value)
    if(feature_value < lower_limit or feature_value > upper_limit):
        print(feature+ ": "+ str(feature_value)+ " is out of range")
        print(feature+ ": "+ str(feature_value)+ " ist außerhalb des Bereichs")
        return False
    else:
        return True


if __name__ == '__main__':
    assert(get_unit_from_feature('30F')=='F')
    assert(get_unit_from_feature('40C')=='C')
    assert(get_value_from_feature('20C') == 20)
    assert(temperature_is_ok('1F') is True)
    assert(temperature_is_ok('45C')is True)
    assert(temperature_is_ok('48C')is False)
    assert(temperature_is_ok('-2C')is False)
    assert(soc_is_ok(20)is True)
    assert(soc_is_ok(15)is False)
    assert(soc_is_ok(80)is True)
    assert(soc_is_ok(90)is False)
    assert(charge_rate_is_ok(0.9)is False)
    assert(charge_rate_is_ok(0.8)is True)
    assert(battery_is_ok('25F', 70, 0.7) is True)
    assert(battery_is_ok('50C', 85, 0) is False)
