import os
import configparser
from funcionarios_final import *
from penetras import gerar_penetras_dict

config = configparser.ConfigParser()
config.read_file(open("dl.cfg"))
BASE_PATH = config["BASE_PATH"]["ROOT"]
START_YEAR = 2020


if __name__ == "__main__":    
    
    try:
        year = int(input("Insira o ano para o qual deseja gerar o relatório (yyyy): "))
    except :
        print("Digite um ano válido (somente números).")
    else:
        if year == 2020:
            admissoes_csv = input("Digite o nome do arquivo csv que contém as admissões: ")

            try:
                admissoes_list = ler_csv(year, admissoes_csv)
            except FileNotFoundError as e:
                print(e)
            except EmptyFileException as e:
                print(e)
            else:
                admissoes_dict = gerar_admissoes_dict(admissoes_list)
                output_file_name = input("Digite o nome do arquivo para gerar como json: ")
                escrever_json_file(year, output_file_name, admissoes_dict)

                # Gerando json penetras
                lista_festa = ler_csv(2020, "festa.csv", False)
                if lista_festa is None:
                    pass
                else:
                    penetras_dict = gerar_penetras_dict(lista_festa, admissoes_dict)
                    escrever_json_file(2020, f"penetras_festa_{year}.json", penetras_dict)
        
        elif year < 2020:
            print("Somente é possível gerar relatórios a partir de 2020.")
        else:
            # Gerenciando admissões para year > 2020
            admissoes_csv = input("Digite o nome do arquivo csv que contém as admissões: ")
            try:
                admissoes_list = ler_csv(year, admissoes_csv)
            except FileNotFoundError as e:
                print(e)
            except EmptyFileException as e:
                print(e)
            else:
                admissoes_dict = gerar_admissoes_dict(admissoes_list)
                
                # Gerenciar demissões para year > 2020
                demissoes_csv = input("Digite o nome do arquivo csv que contém as demissões. Se não houver demissões, deixe em branco: ")
                
                if demissoes_csv == "": confirma_em_branco = input("Você deixou em branco o arquivo demissões. Confirma (s/n)? ")
                
                while demissoes_csv == "":
                    if confirma_em_branco.lower() == "s":
                        break
                    elif confirma_em_branco.lower() == "n":
                        demissoes_csv = input("Digite o nome do arquivo csv que contém as demissões. Se não houver demissões, deixe em branco: ")
                        if demissoes_csv == "": confirma_em_branco = input("Você deixou em branco o arquivo demissões. Confirma (s/n)? ")
                    else:
                        print("Opção inválida.")
                        confirma_em_branco = input("Você deixou em branco o arquivo demissões. Confirma (s/n)? ")
                
                if demissoes_csv == "":
                    # fluxo sem demissoes
                    
                    # ler o final_report ano anterior
                    previous_final_report_name = input(f"Digite o nome do relatório do ano anterior ({year-1}): ")
                    try:
                        previous_year_report = ler_json_file(year-1, previous_final_report_name)
                    except FileNotFoundError as e:
                        print(e)
                    except EmptyFileException as e:
                        print(e)
                    else:
                        output_file_name = input("Digite o nome do arquivo para gerar como json: ")
                        final_report = relatorio_final_funcionarios(year, previous_year_report, admissoes_dict)
                        escrever_json_file(year, output_file_name, final_report)
                else:
                    # fluxo com demissoes
                    pass
                        
                        

                # else:
                    # demissoes_list = ler_csv(year, demissoes_csv)
                    # pass

                    
            
            
            # if ler_csv(year, admissoes_csv) is not None:
            #     admissoes_list = ler_csv(year, admissoes_csv)
            #     admissoes_dict = gerar_admissoes_dict(admissoes_list)

            #     # Gerenciando demissões
            #     demissoes_csv = input("Digite o nome do arquivo csv que contém as demissões: ")
            #     if ler_csv(year, demissoes_csv) is not None:
            #         demissoes_list = ler_csv(year, demissoes_csv)
            #         demissoes_dict = gerar_admissoes_dict(demissoes_list)

            #         # Gerando log demissões
            #         escrever_json_file(year, f"log_demissões_{year}.json", demissoes_dict)

            #         previous_final_report_name = input(f"Digite o nome do relatório do ano anterior ({year-1}): ")
            #         previous_final_report_path = f"{BASE_PATH}/{year-1}/{previous_final_report_name}"
                    
            #         try:
            #             assert os.path.isfile(previous_final_report_path) is True
            #         except:
            #             print(f"O arquivo {previous_final_report_name} não existe.")
            #         else:
            #             previous_year_report = ler_json_file(previous_final_report_path)
            #             try:
            #                 assert previous_year_report is not None
            #             except:
            #                 print(f"O arquivo {previous_final_report_name} está vazio.")
            #             else:
            #                 output_file_name = input("Digite o nome do arquivo para gerar como json: ")
            #                 relatorio_final_funcionarios(year, 
            #                                             output_file_name, 
            #                                             admissoes_dict, demissoes_dict, 
            #                                             previous_year_report)
            #     else:
            #         previous_final_report_name = input(f"Digite o nome do relatório do ano anterior ({year-1}): ")
            #         previous_final_report_path = f"{BASE_PATH}/{year-1}/{previous_final_report_name}"
                    
            #         try:
            #             assert os.path.isfile(previous_final_report_path) is True
            #         except:
            #             print(f"O arquivo {previous_final_report_name} não existe.")
            #         else:
            #             previous_year_report = ler_json_file(previous_final_report_path)
            #             try:
            #                 assert previous_year_report is not None
            #             except:
            #                 print(f"O arquivo {previous_final_report_name} está vazio.")
            #             else:
            #                 output_file_name = input("Digite o nome do arquivo para gerar como json: ")
            #                 relatorio_final_funcionarios(year, 
            #                                             output_file_name, 
            #                                             admissoes_dict, 
            #                                             previous_year_report)
                    
                            
            #     # Gerando penetras .json
            #     lista_festa = ler_csv(year, "festa.csv")
            #     penetras_dict = gerar_penetras_dict(lista_festa, f"{BASE_PATH}/{year}/{output_file_name}")
            #     escrever_json_file(year, f"penetras_festa{year}.json", penetras_dict)
