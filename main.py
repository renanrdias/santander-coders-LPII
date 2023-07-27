import os







if __name__ == "__main__":
    os.system("python3 tests.py")
    while True:
        answer = input("Deseja gerar os relatórios para mais um ano?\n1 - Sim\n2 - Não\n")
        try:
            int(answer)
        except:
            print("Opção inválida.")
            continue
        else:
            if int(answer) != 1 and int(answer) != 2:
                print("Opção inválida")
            elif int(answer) == 1:
                os.system("python3 tests.py")
            else:
                break


            

