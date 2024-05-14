from tkinter import *
from PIL import Image, ImageTk
import uuid 
import json
from tkinter import Frame, Label, Button, Entry, Toplevel

class Application:
    def __init__(self, master=None):
        self.master = master
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="MENU INICIAL")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        self.scrum = Button(self.widget1, text="SCRUM", font=("Calibri", "12"), width=10, command=self.open_scrum)
        self.scrum.pack()

        self.kanban = Button(self.widget1, text="KANBAN", font=("Calibri", "12"), width=10, command=self.open_kanban)
        self.kanban.pack()

        self.xp = Button(self.widget1, text="XP", font=("Calibri", "12"), width=10, command=self.open_xp)
        self.xp.pack()

    def open_scrum(self):
        newWindow = Toplevel(self.master)
        newWindow.title("SCRUM")
        MenuScrum(newWindow)

    def open_kanban(self):
        newWindow = Toplevel(self.master)
        newWindow.title("KANBAN")
        MenuKanban(newWindow)

    def open_xp(self):
        newWindow = Toplevel(self.master)
        newWindow.title("XP")
        MenuXP(newWindow)


class MenuScrum:
    def __init__(self, master=None):
        self.master = master
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="MENU SCRUM")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.carregar_dados()


        self.cadastrar_sprint = Button(self.widget1, text="CADASTRAR SPRINT", font=("Calibri", "12"), width=20,
                                       command=self.cadastra_sprint)
        self.cadastrar_sprint.pack()
        self.cadastrar_historia = Button(self.widget1, text="CADASTRAR HISTÓRIA", font=("Calibri", "12"), width=20,
                                         command=self.cadastra_historia)
        self.cadastrar_historia.pack()

        self.cadastrar_tarefas = Button(self.widget1, text="CADASTRAR TAREFAS", font=("Calibri", "12"), width=20,
                                        command=self.cadastra_tarefas)
        self.cadastrar_tarefas.pack()

        self.visualizar_dados = Button(self.widget1, text="VISUALIZAR DADOS", font=("Calibri", "12"), width=20,
                                       command=self.visualizar_dados)
        self.visualizar_dados.pack()

    def salvar_dados(self):
        with open('scrum_data.json', 'w') as f:
            json.dump(self.scrum_data, f, indent=4)
    def carregar_dados(self):
        try:
            with open('scrum_data.json', 'r') as f:
                self.scrum_data = json.load(f)
        except FileNotFoundError:
            self.scrum_data = {"sprints": [], "historias": [], "tarefas": []}
        
    def cadastra_sprint(self):
        newWindow2 = Toplevel(self.master)
        newWindow2.title("Cadastrar Sprint")
        Label(newWindow2, text="Digite os detalhes da Sprint:").pack()
        entry = Entry(newWindow2)
        entry.pack()
        Button(newWindow2, text="Salvar", command=lambda: self.salvar_sprint(entry.get())).pack()
        Button(newWindow2, text="Voltar", command=newWindow2.destroy).pack()

    def cadastra_historia(self):
        newWindow2 = Toplevel(self.master)
        newWindow2.title("Cadastrar História")
        Label(newWindow2, text="Digite os detalhes da História:").pack()
        entry = Entry(newWindow2)
        entry.pack()
        Button(newWindow2, text="Salvar", command=lambda: self.salvar_historia(entry.get())).pack()
        Button(newWindow2, text="Voltar", command=newWindow2.destroy).pack()

    def cadastra_tarefas(self):
        newWindow2 = Toplevel(self.master)
        newWindow2.title("Cadastrar Tarefas")
        Label(newWindow2, text="Digite os detalhes das Tarefas:").pack()
        entry = Entry(newWindow2)
        entry.pack()
        Button(newWindow2, text="Salvar", command=lambda: self.salvar_tarefa(entry.get())).pack()
        Button(newWindow2, text="Voltar", command=newWindow2.destroy).pack()

    def visualizar_dados(self):
        print("Sprints:", self.scrum_data["sprints"])
        print("Histórias:", self.scrum_data["historias"])
        print("Tarefas:", self.scrum_data["tarefas"])

    def salvar_sprint(self, sprint_details):
        self.scrum_data["sprints"].append(sprint_details)
        self.salvar_dados()  # Salva dados após adição
        print("Sprint cadastrada com sucesso!")
        print("Dados do SCRUM:", self.scrum_data)

    def salvar_historia(self, historia_details):
        self.scrum_data["historias"].append(historia_details)
        self.salvar_dados()  # Salva dados após adição
        print("História cadastrada com sucesso!")
        print("Dados do SCRUM:", self.scrum_data)

    def salvar_tarefa(self, tarefa_details):
        self.scrum_data["tarefas"].append(tarefa_details)
        self.salvar_dados()  # Salva dados após adição
        print("Tarefa cadastrada com sucesso!")
        print("Dados do SCRUM:", self.scrum_data)



class MenuKanban:
    def __init__(self, master=None):
        self.master = master
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="MENU KANBAN")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.carregar_dados()

        self.todo_btn = Button(self.widget1, text="Para fazer", font=("Calibri", "12"), width=10, command=lambda: self.show_entry_popup("Para fazer"))
        self.todo_btn.pack()

        self.in_progress_btn = Button(self.widget1, text="Em progresso", font=("Calibri", "12"), width=10,
                                      command=lambda: self.show_entry_popup("Em progresso"))
        self.in_progress_btn.pack()

        self.done_btn = Button(self.widget1, text="Pronto", font=("Calibri", "12"), width=10, command=lambda: self.show_entry_popup("Pronto"))
        self.done_btn.pack()

        self.approved_btn = Button(self.widget1, text="Aprovado", font=("Calibri", "12"), width=10,
                                   command=lambda: self.show_entry_popup("Aprovado"))
        self.approved_btn.pack()

        self.visualizar_dados_btn = Button(self.widget1, text="VISUALIZAR DADOS", font=("Calibri", "12"), width=20,
                                           command=self.visualizar_dados)
        self.visualizar_dados_btn.pack()
        self.state_map = {
            "Para fazer": "todo",
            "Em progresso": "in_progress",
            "Pronto": "done",
            "Aprovado": "approved"
        }

    def salvar_dados(self):
        with open('kanban_data.json', 'w') as f:
            json.dump(self.kanban_data, f, indent=4)

    def carregar_dados(self):
        try:
            with open('kanban_data.json', 'r') as f:
                self.kanban_data = json.load(f)
        except FileNotFoundError:
            self.kanban_data = {"todo": [], "in_progress": [], "done": [], "approved": []}

    def show_entry_popup(self, state):
        popup = Toplevel(self.master)
        popup.title(state)
        Label(popup, text=f"Digite os detalhes para {state}:").pack()

        entry = Entry(popup)
        entry.pack()
        Button(popup, text="Salvar", command=lambda: self.save_entry(state, entry.get())).pack()
        Button(popup, text="Voltar", command=popup.destroy).pack()

    def save_entry(self, state, text):
        state_key = state.replace(" ", "_")
        if state_key not in self.kanban_data:
            self.kanban_data[state_key] = []  # Inicializa a chave se não existir
        self.kanban_data[state_key].append(text)
        self.salvar_dados()  # Salva os dados após adição
        print(f"Tarefa '{text}' adicionada com sucesso em '{state}'.")


    def excluir_tarefa(self, state, index):
        del self.kanban_data[state.replace(" ", "_")][index]
        self.salvar_dados()  # Salva os dados após exclusão
        print(f"Tarefa excluída com sucesso de '{state}'.")

    def visualizar_dados(self):
        popup = Toplevel(self.master)
        popup.title("Dados do Kanban")

        container = Frame(popup)
        container.pack(padx=10, pady=10)

        for state, tasks in self.kanban_data.items():
            state_label = Label(container, text=f"{state.capitalize().replace('_', ' ')}:", font=("bold", 12))
            state_label.pack(fill='x', pady=(10, 5))
            
            if not tasks:  # Se a lista estiver vazia, adicione um feedback visual
                no_task_label = Label(container, text="Nenhuma tarefa.", font=("italic",))
                no_task_label.pack(fill='x')
            
            for idx, task in enumerate(tasks):
                task_label = Label(container, text=f"{idx + 1}. {task}")
                task_label.pack(fill='x')

                # Botão de exclusão para cada tarefa
                delete_btn = Button(container, text="Excluir", command=lambda s=state, i=idx: self.excluir_tarefa(s, i))
                delete_btn.pack()

        # Botão de fechar no fim para melhor acessibilidade
        close_btn = Button(popup, text="Fechar", command=popup.destroy)
        close_btn.pack(pady=10)


        
class MenuXP:
    def __init__(self, master=None, releases=None):
        self.master = master
        self.tarefas = {}  

        self.releases = releases if releases is not None else []
        self.master = master
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="MENU XP")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        self.cadastrar_release_btn = Button(self.widget1, text="Cadastrar Release", font=("Calibri", "12"), width=20,
                                            command=self.cadastrar_release)
        self.cadastrar_release_btn.pack()

        self.cadastrar_iteracao_btn = Button(self.widget1, text="Cadastrar Iteração", font=("Calibri", "12"), width=20,
                                              command=self.cadastrar_iteracao)
        self.cadastrar_iteracao_btn.pack()

        self.cadastrar_historia_btn = Button(self.widget1, text="Cadastrar História", font=("Calibri", "12"), width=20,
                                             command=self.cadastrar_historia)
        self.cadastrar_historia_btn.pack()

        self.cadastrar_tarefa_btn = Button(self.widget1, text="Cadastrar Tarefa", font=("Calibri", "12"), width=20,
                                            command=self.cadastrar_tarefa)
        self.cadastrar_tarefa_btn.pack()

        self.rel_release_btn = Button(self.widget1, text="Relatório de Releases", font=("Calibri", "12"), width=20,
                                      command=self.rel_release)
        self.rel_release_btn.pack()
        self.estado_ativo = None  # Acompanha o estado (Listbox) ativo

        self.rel_sprints_btn = Button(self.widget1, text="Relatório de Sprints", font=("Calibri", "12"), width=20,
                                      command=self.rel_sprints)
        self.rel_sprints_btn.pack()

        self.rel_tarefas_btn = Button(self.widget1, text="Relatórios de Tarefas", font=("Calibri", "12"), width=20,
                                      command=self.rel_tarefas)
        self.rel_tarefas_btn.pack()

        self.kanban_board_btn = Button(self.widget1, text="Kanban Board", font=("Calibri", "12"), width=20,
                                       command=self.kanban_board)
        self.kanban_board_btn.pack()

        self.excluir_dados_btn = Button(self.widget1, text="Excluir Todos os Dados", font=("Calibri", "12"), width=20,
                                        command=self.excluir_todos_dados)
        self.excluir_dados_btn.pack()






        self.carregar_dados()  
    def cadastrar_release(self):
        newWindow = Toplevel(self.master)
        newWindow.title("Cadastrar Release")

        Label(newWindow, text="Título da Release:").pack()
        titulo_entry = Entry(newWindow)
        titulo_entry.pack()

        Label(newWindow, text="Ordem da Release:").pack()
        ordem_entry = Entry(newWindow)
        ordem_entry.pack()

        Label(newWindow, text="Data de Início (DD/MM/AAAA):").pack()
        inicio_entry = Entry(newWindow)
        inicio_entry.pack()

        Label(newWindow, text="Data Final (DD/MM/AAAA):").pack()
        final_entry = Entry(newWindow)
        final_entry.pack()
        Button(newWindow, text="Salvar", command=lambda: self.salvar_release(
            titulo=titulo_entry.get(), 
            ordem=ordem_entry.get(), 
            inicio=inicio_entry.get(), 
            final=final_entry.get(),
            window=newWindow)).pack()
        
    def carregar_dados(self):
        try:
            with open('xp_data.json', 'r') as file:
                self.releases = json.load(file)
        except FileNotFoundError:
            self.releases = []

    def salvar_dados(self):
        with open('xp_data.json', 'w') as file:
            json.dump(self.releases, file, indent=4)

    def salvar_release(self, titulo, ordem, inicio, final, window):
        self.releases.append({
            "titulo": titulo,
            "ordem": ordem,
            "inicio": inicio,
            "final": final
        })
        self.salvar_dados()
        window.destroy()
        print("Release salva com sucesso!")

    def cadastrar_iteracao(self):
        newWindow = Toplevel(self.master)
        newWindow.title("Cadastrar Iteração")
        
        Label(newWindow, text="Nome da Release:").pack()
        release_id_entry = Entry(newWindow)
        release_id_entry.pack()

        Label(newWindow, text="Data de Início (DD/MM/AAAA):").pack()
        inicio_entry = Entry(newWindow)
        inicio_entry.pack()

        Label(newWindow, text="Data Final (DD/MM/AAAA):").pack()
        final_entry = Entry(newWindow)
        final_entry.pack()

        Button(newWindow, text="Salvar", command=lambda: self.salvar_iteracao(
            release_id=release_id_entry.get(), 
            inicio=inicio_entry.get(), 
            final=final_entry.get(),
            window=newWindow)).pack()


    def salvar_iteracao(self, release_id, inicio, final, window):
        for release in self.releases:
            if release["titulo"] == release_id:  # Simples comparação por título
                if "iteracoes" not in release:
                    release["iteracoes"] = []
                release["iteracoes"].append({"inicio": inicio, "final": final})
                break
        self.salvar_dados()
        window.destroy()
        print("Iteração salva com sucesso!")

    def cadastrar_historia(self):
        newWindow = Toplevel(self.master)
        newWindow.title("Cadastrar História")

        Label(newWindow, text="Nome da Iteração:").pack()
        iteracao_id_entry = Entry(newWindow)
        iteracao_id_entry.pack()

        Label(newWindow, text="Título da História:").pack()
        titulo_entry = Entry(newWindow)
        titulo_entry.pack()

        Label(newWindow, text="Descrição da História:").pack()
        descricao_entry = Entry(newWindow)
        descricao_entry.pack()

        Label(newWindow, text="Valor do Story Points:").pack()
        story_points_entry = Entry(newWindow)
        story_points_entry.pack()

        Button(newWindow, text="Salvar", command=lambda: self.salvar_historia(
            iteracao_id=iteracao_id_entry.get(),
            titulo=titulo_entry.get(),
            descricao=descricao_entry.get(),
            story_points=story_points_entry.get(),
            window=newWindow)).pack()
        
    def salvar_historia(self, iteracao_id, titulo, descricao, story_points, window):
        for release in self.releases:
            for iteracao in release.get("iteracoes", []):
                if iteracao["inicio"] == iteracao_id:  # Simples comparação por data de início
                    if "historias" not in iteracao:
                        iteracao["historias"] = []
                    iteracao["historias"].append({"titulo": titulo, "descricao": descricao, "story_points": story_points})
                    break
        self.salvar_dados()
        window.destroy()
        print("História salva com sucesso!")
        

    def cadastrar_tarefa(self):
        newWindow = Toplevel(self.master)
        newWindow.title("Cadastrar Tarefa")

        Label(newWindow, text="ID da História:").pack()
        historia_id_entry = Entry(newWindow)
        historia_id_entry.pack()

        Label(newWindow, text="Descrição da Tarefa:").pack()
        descricao_entry = Entry(newWindow)
        descricao_entry.pack()

        Label(newWindow, text="Responsável pela Implementação:").pack()
        responsavel_entry = Entry(newWindow)
        responsavel_entry.pack()

        Button(newWindow, text="Salvar", command=lambda: self.salvar_tarefa(
            historia_id=historia_id_entry.get(),
            descricao=descricao_entry.get(),
            responsavel=responsavel_entry.get(),
            window=newWindow)).pack()
    

    def salvar_tarefa(self, historia_id, descricao, responsavel, window):
        for release in self.releases:
            for iteracao in release.get("iteracoes", []):
                for historia in iteracao.get("historias", []):
                    if historia["titulo"] == historia_id:  # Simples comparação por título
                        if "tarefas" not in historia:
                            historia["tarefas"] = []
                        historia["tarefas"].append({"descricao": descricao, "responsavel": responsavel})
                        break
        self.salvar_dados()
        window.destroy()
        print("Tarefa salva com sucesso!")

    def rel_release(self):
        print("Relatório de Releases")
        if not self.releases:  # Verifica se a lista de releases está vazia
            print("Nenhuma release cadastrada.")
            return

        for release in self.releases:
            print(f"\nRelease: {release['titulo']}")
            print(f"Ordem: {release.get('ordem', 'Não especificado')}")
            print(f"Início: {release.get('inicio', 'Não especificado')}")
            print(f"Final: {release.get('final', 'Não especificado')}")

            # Se a release tiver iterações, imprime as informações básicas de cada iteração
            if "iteracoes" in release and release["iteracoes"]:
                print("Iterações:")
                for iteracao in release["iteracoes"]:
                    print(f"\tDe {iteracao.get('inicio', 'Data não especificada')} a {iteracao.get('final', 'Data não especificada')}")
                    # Se desejar, adicione mais detalhes sobre as histórias e tarefas de cada iteração
            else:
                print("\tNenhuma iteração cadastrada nesta release.")

            # Adicional: Se quiser listar histórias diretamente sob releases (se aplicável)
            if "historias" in release and release["historias"]:
                print("Histórias:")
                for historia in release["historias"]:
                    print(f"\tHistória: {historia.get('titulo', 'Título não especificado')}")
                    # Detalhes adicionais sobre histórias podem ser adicionados aqui
            else:
                pass

    def rel_sprints(self):
        print("Relatório de Sprints (Iterações)")
        for release in self.releases:
            print(f"\nRelease: {release['titulo']}")
            for iteracao in release.get("iteracoes", []):  # Assume que a chave correta é "iteracoes"
                print(f"Iteração de {iteracao['inicio']} a {iteracao['final']}:")
                for historia in iteracao.get("historias", []):  # Verifica se existem histórias na iteração
                    print(f"\tHistória {historia['titulo']}: {historia['descricao']}")

    def rel_tarefas(self):
        print("Relatórios de Tarefas")
        for release in self.releases:
            print(f"\nRelease: {release['titulo']}")
            # Verifica se a release tem iterações, se não, continua para a próxima release
            if "iteracoes" not in release:
                continue
            for iteracao in release.get("iteracoes", []):
                print(f"Iteração de {iteracao['inicio']} a {iteracao['final']}:")

                # Verifica se a iteração tem histórias, se não, continua para a próxima iteração
                if "historias" not in iteracao:
                    continue
                for historia in iteracao.get("historias", []):
                    print(f"\tHistória {historia['titulo']}:")

                    if "tarefas" not in historia:
                        continue
                    for tarefa in historia.get("tarefas", []):
                        print(f"\t\tTarefa {tarefa.get('descricao', 'Sem descrição')} - Responsável: {tarefa.get('responsavel', 'Não atribuído')}")

    def kanban_board(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Kanban Board")
        Label(self.newWindow, text="KANBAN BOARD").pack()

        Button(self.newWindow, text="Adicionar Tarefa", command=self.adicionar_tarefa).pack(pady=10)
        Button(self.newWindow, text="Excluir Tarefa", command=self.excluir_tarefa_selecionada).pack(pady=10)

        # Inicializa self.listboxes aqui, antes de tentar usá-lo
        self.listboxes = {}

        for state in ["Para fazer", "Em progresso", "Pronto", "Aprovado"]:
            frame = Frame(self.newWindow)
            frame.pack(side=LEFT, padx=10, pady=10)
            Label(frame, text=state).pack()
            listbox = Listbox(frame)
            listbox.bind('<<ListboxSelect>>', lambda e, s=state: self.selecionar_estado(e, s))
            self.listboxes[state] = listbox
            for task_desc in self.get_tasks_by_state(state):
                listbox.insert(END, task_desc)
            listbox.pack(side=LEFT, fill=BOTH)

    def get_tasks_by_state(self, state):
        """Retorna as descrições das tarefas que correspondem ao estado fornecido."""
        return [tarefa["descricao"] for tarefa in self.tarefas.values() if tarefa["estado"] == state]
    def selecionar_estado(self, event, state):
        """Define o estado atual baseado na seleção do Listbox."""
        self.estado_ativo = state

    def excluir_todos_dados(self):
        self.releases = []
        self.tarefas = []
        # Salva o estado vazio
        self.salvar_dados()
        print("Todos os dados foram excluídos.")
    def adicionar_tarefa(self):
        newWindow = Toplevel(self.master)
        newWindow.title("Adicionar Nova Tarefa")

        Label(newWindow, text="Descrição da Tarefa:").pack()
        descricao_entry = Entry(newWindow)
        descricao_entry.pack()

        Label(newWindow, text="Estado:").pack()
        estado_entry = Entry(newWindow)  # Idealmente, substitua por um OptionMenu
        estado_entry.pack()

        Button(newWindow, text="Salvar", command=lambda: self.salvar_nova_tarefa(
            descricao=descricao_entry.get(),
            estado=estado_entry.get(),
            window=newWindow
        )).pack()

    def excluir_tarefa_selecionada(self):
        if not self.estado_ativo or not self.listboxes[self.estado_ativo].curselection():
            print("Nenhuma tarefa selecionada.")
            return
        selected_index = self.listboxes[self.estado_ativo].curselection()[0]
        task_ids = [task_id for task_id, task in self.tarefas.items() if task["estado"] == self.estado_ativo]
        if task_ids:
            selected_task_id = task_ids[selected_index]
            del self.tarefas[selected_task_id]  # Remove a tarefa do dicionário
            self.salvar_dados()
            self.kanban_board()  # Atualiza o quadro Kanban
            print("Tarefa excluída com sucesso.")
        else:
            print("Erro ao identificar a tarefa selecionada.")

    def salvar_nova_tarefa(self, descricao, estado, window):
        if estado not in ["Para fazer", "Em progresso", "Pronto", "Aprovado"]:
            print("Estado inválido.")
            return
        task_id = str(uuid.uuid4())  # Gera um ID único
        self.tarefas[task_id] = {"descricao": descricao, "estado": estado}
        self.salvar_dados()
        window.destroy()
        self.kanban_board()  # Atualiza o quadro Kanban

root = Tk()
app = Application(master=root)
root.mainloop()