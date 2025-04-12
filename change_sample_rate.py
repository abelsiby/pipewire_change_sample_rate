import os


def get_default_and_other_sample_rates(default_samp):
    """
    Prompts the user to enter n integers and stores them in a list.

    Args:
        default_samp (int): The deault sample rate in Hz to get from the user.

    Returns:
        list: A list containing other sample rates entered by the user.

    Raises:
        TypeError: If n is not an integer or is less than 1.
        ValueError: If the user enters a non-integer value.
    """
    if not isinstance(default_samp, int) or default_samp < 1:
        raise TypeError("Invalid value for default sample rate. n must be a positive integer.")

    integer_list = []
    while True:
        try:
            nums = str(input(f"Enter other sample rates: "))
            integer_list = [int(n) for n in nums.split(" ")]
            integer_list.append(default_samp)
            integer_list.sort()
            print("List of other sample rates:", integer_list)
            break

        except ValueError:
            print("Invalid other sample rates. Please enter values followed by a single space, in Hz.")

    return integer_list


def create_configs_from_list(def_rate, rates_list, pipewire_conf="~/.config/pipewire/pipewire.conf.d/pipewire-hifi.conf", client_conf="~/.config/pipewire/client.conf.d/client-hifi.conf"):
    """
    Creates a .conf file where the 'default.clock.allowed-rates' values
    are taken from the provided data_list.

    Args:
        data_list (list): The list of integer values to use for allowed rates.
        filename (str, optional): The name of the file to create.
                                   Defaults to "myconf.conf".
    """
    pipewirefol = os.path.dirname(pipewire_conf)
    os.makedirs(pipewirefol, exist_ok=True)

    clientfol = os.path.dirname(client_conf)
    os.makedirs(clientfol, exist_ok=True)
    
    def_rate = str(def_rate)
    allowed_rates_str = " ".join(map(str, rates_list))

    client_config_content = f"""
stream.properties = {{
    resample.quality = 14
}}
"""
    pipewire_config_content = f"""
context.properties = {{
    default.clock.rate = {def_rate}
    default.clock.allowed-rates = [ {allowed_rates_str} ]
}}
"""

    try:
        with open(pipewire_conf, 'w') as f:
            f.write(pipewire_config_content.strip() + '\n')
        print(f"Successfully created the file '{os.path.basename(pipewire_conf)}' with default sample rate: {def_rate} and allowed rates: {rates_list}")
    except Exception as e:
        print(f"An error occurred while creating the file {os.path.basename(pipewire_conf)}: {e}")

    try:
        with open(client_conf, 'w') as f:
            f.write(client_config_content.strip() + '\n')
        print(f"Successfully created the file '{os.path.basename(client_conf)}'")
    except Exception as e:
        print(f"An error occurred while creating the file {os.path.basename(client_conf)}: {e}")


if __name__ == "__main__":
    while True:
        try:
            def_samp_rate = int(input("Enter the default sample rate: "))
            if def_samp_rate < 1:
                print("Please enter a positive integer for default sample rate.")
                continue
            break
        except ValueError:
            print("Invalid value for default sample rate. Please enter sample rate in Hz.")

    try:
        rates_list = get_default_and_other_sample_rates(def_samp_rate)
        create_configs_from_list(def_samp_rate, rates_list)

    except (TypeError, ValueError) as e:
        print(e)
