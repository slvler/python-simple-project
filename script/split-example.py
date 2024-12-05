def main():
    print("Email lancer")
    print("")

    email = input('Input your email address: ')

    (username, domain) = email.split('@')
    (domain, extension) = domain.split(".")

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)




main()