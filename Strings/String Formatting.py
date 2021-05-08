def print_formatted(k):
    def bina(n):
        rep = bin(n)[2:]
        pad = m - len(rep)
        return pad * " " + rep


    def inta(n):
        rep = str(n)
        pad = m - len(rep)
        return pad * " " + rep + " "

    def octa(n):
        rep = oct(n)[2:]
        pad = m - len(rep)
        return pad * " " + rep + " "

    def hexa(n):   
        rep = hex(n)[2:].upper()
        pad = m - len(rep)
        return pad * " " + rep + " "

    m = len(bin(k).lstrip("0b"))
    for i in range(1, k+1):
        r = [inta(i), octa(i), hexa(i), bina(i)]
        print("".join(r))
    


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)