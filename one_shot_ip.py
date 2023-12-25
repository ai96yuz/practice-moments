from requests import get

lblue = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"


banner = f"""
{red} ░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆
{red} ░███████████████████████████████      ███{ylw}ONE_SHOT_IP{red}███
{red} ░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓◤
{red} ╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░       {lblue}# {grn}User Data Finder by {ylw}ONE_SHOT_IP
{red} ▒░░▓▓▓▓▓▓█▄▄▄▄▄█▀╬░       {lblue}# {grn}Coded by {ylw}Someone
{red} ░░█▓▓▓▓▓▌░▒▒▒▒▒▒▒▒▒       {lblue}# {grn}GitHub ID {red}::: {lblue}None
{red} ░▐█▓▓▓▓▓░░▒▒▒▒▒▒▒▒▒       {lblue}# {grn}Version {red}0.1
{red} ░▐██████▌╬░▒▒▒▒▒▒▒▒       {lblue}# {grn}Have a fun!
"""


def print_help():
    help_text = f"""
    {red}Usage {ylw}: {grn}python one_shot_ip.py [OPTION] ...
    {ylw}To get IP information

    Mandatory arguments to long options are mandatory for short options too
        {red}-h {ylw}, {red}--help         {grn}display this help and exit
        {red}-I {ylw}, {red}--ip           {grn}To get IP information

    {ylw}Use help 

        {grn}python {red}IPLocation.py {ylw}--ip{red}/{ylw}-I {red}[{grn}IP ADDRESS{red}]
    """
    print(banner)
    print(help_text)


def get_ip_location(IP):
    try:
        result = get(f'http://ip-api.com/json/{IP}').json()

        print(f"""
    {grn}[{red}+{grn}] {lblue}COUNTRY {red}::: {ylw}{result['country']}
    {grn}[{red}+{grn}] {lblue}COUNTRY CODE {red}::: {ylw}{result['countryCode']}
    {grn}[{red}+{grn}] {lblue}REGION {red}::: {ylw}{result['region']}
    {grn}[{red}+{grn}] {lblue}REGION NAME {red}::: {ylw}{result['regionName']}
    {grn}[{red}+{grn}] {lblue}CITY {red}::: {ylw}{result['city']}
    {grn}[{red}+{grn}] {lblue}ZIP {red}::: {ylw}{result['zip']}
    {grn}[{red}+{grn}] {lblue}LAT {red}::: {ylw}{result['lat']}
    {grn}[{red}+{grn}] {lblue}LON {red}::: {ylw}{result['lon']}
    {grn}[{red}+{grn}] {lblue}TIME ZONE {red}::: {ylw}{result['timezone']}
    {grn}[{red}+{grn}] {lblue}ISP {red}::: {ylw}{result['isp']}
    {grn}[{red}+{grn}] {lblue}ORG {red}::: {ylw}{result['org']}
    {grn}[{red}+{grn}] {lblue}AS {red}::: {ylw}{result['as']}
    {grn}[{red}+{grn}] {lblue}QUERY {red}::: {ylw}{result['query']}
    {grn}[{red}+{grn}] {lblue}GOOGLE MAP {red}::: {ylw}https://www.google.com/maps?q={result['lat']},{result['lon']}
""")
    except Exception as e:
        print(f" {red}[{ylw}!{red}] Error: {e}")


def main():
    print_help()
    while True:
        try:
            option = input("Enter an option ('q' to quit): ")
            if option.lower() == 'q':
                break
            elif option == "--ip" or option == "-I":
                ip = input("Enter IP address: ")
                get_ip_location(ip)
            elif option == "--help" or option == "-h":
                print_help()
            else:
                print(f"    {red}[{ylw}!{red}] This is not a valid option. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
