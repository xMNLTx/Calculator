import flet as ft


def main(page):

    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.Column]()

    def btn_click(e):
        greetings.current.controls.append(
            ft.Text(
                f"Привет, {first_name.current.value} {last_name.current.value}!!!")
        )
        first_name.current.value = ""
        last_name.current.value = ""
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref=first_name, label="Введи имя", autofocus=True),
        ft.TextField(ref=last_name, label="Введи фамилию"),
        ft.ElevatedButton("Приветствие!", on_click=btn_click),
        ft.Column(ref=greetings),
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)


ft.app(main)
