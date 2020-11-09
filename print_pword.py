# import crypto
import password

def main():
    # print('Generating password...')
    psswrd = password.get_password()
    #print(psswrd)
    print("USE pssword; INSERT INTO psswrds(location, psswrd) VALUES (sha('cupcake'), sha1('" + psswrd + "'));")

main()