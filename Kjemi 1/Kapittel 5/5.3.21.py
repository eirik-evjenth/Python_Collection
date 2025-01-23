import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_molar_mass(C, H, O, N):
    return C * 12.01 + H * 1.008 + O * 16.00 + N * 14.01

def main():
    print("Velkommen til molar masse kalkulatoren!")
    print("Vennligst oppgi antall atomer for hvert element i forbindelsen din.")
    
    try:
        C_atomer = int(input("Antall karbonatomer (C): "))
        H_atomer = int(input("Antall hydrogenatomer (H): "))
        O_atomer = int(input("Antall oksygenatomer (O): "))
        N_atomer = int(input("Antall nitrogenatomer (N): "))
    except ValueError:
        print("Ugyldig input! Vennligst oppgi et heltall.")
        return
    
    clear()
    Molar_masse = calculate_molar_mass(C_atomer, H_atomer, O_atomer, N_atomer)
    print(f"\nDen molare massen av forbindelsen er {round(Molar_masse, 2)} g/mol")
    time.sleep(3)  # Pause for 3 seconds
    clear()

    try:
        masse = float(input("\nHvor mange gram har du av dette stoffet? "))
    except ValueError:
        print("Ugyldig input! Vennligst oppgi et tall.")
        return
    
    clear()
    antall_mol = masse / Molar_masse
    print(f"Antall mol av stoffet er {round(antall_mol, 2)} mol")
    time.sleep(3)  # Pause for 3 seconds
    clear()
    
    # Additional functionality: Calculate the number of molecules
    avogadro_number = 6.022e23
    antall_molekyler = antall_mol * avogadro_number
    print(f"Antall molekyler av stoffet er {antall_molekyler:.2e}")
    time.sleep(3)
    clear()

if __name__ == "__main__":
    main()