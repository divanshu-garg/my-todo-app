import streamlit
import functions

todos = functions.get_todos()


def add_todo():
    todo = streamlit.session_state["new_todo"] + ' \n'
    todos.append(todo)
    functions.write_todos(todos)


streamlit.title("My Todo app")
streamlit.subheader("This is my todo app. ")
streamlit.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    print(index, todo)
    checkbox = streamlit.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

streamlit.text_input(label="Add todo:", placeholder="Enter a new todo: ",
                     on_change=add_todo, key="new_todo")


streamlit.session_state

