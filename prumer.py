import sys

def prumer(cisla):
    soucet = 0
    for i in cisla:
        soucet += 1
    return(soucet/len(cisla))
    











"""
def main():
    if len(sys.argv) < 2:
        print("Zadejte řadu čísel oddělených mezerou")
        return

    try:
        cisla = [float(arg) for arg in sys.argv[1:]]
        avg = sum(cisla) / len (cisla)
        print (f"Průměr je {avg}")
    except ValueError: 
        print("Umím průměrovat pouze čísla")

if __name__ == '__main__':
    main()
"""