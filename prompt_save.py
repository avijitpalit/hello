import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import json

SPACING = 10

def create_custom_dialog():
    dialog = Gtk.Dialog(title="Custom Dialog", parent=None, flags=0, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))

    # Get the content area
    content_area = dialog.get_content_area()

    # Add widgets to the content area
    label = Gtk.Label(label="This is a custom dialog")
    content_area.add(label)

    dialog.show_all()
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        print("OK clicked")
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancel clicked")
    dialog.destroy()

def create_table():
    grid = Gtk.Grid(row_spacing=SPACING, column_spacing=SPACING)

    # Create some labels as table cells
    label1 = Gtk.Label(label="Prompt:")
    label1.set_halign(Gtk.Align.START)
    label2 = Gtk.Label(label="Negative Prompt:")
    label2.set_halign(Gtk.Align.START)

    prompt = Gtk.Entry()
    prompt.set_hexpand(True)
    prompt.set_placeholder_text("Prompt")

    neg_prompt = Gtk.Entry()
    neg_prompt.set_hexpand(True)
    neg_prompt.set_placeholder_text("Negative Prompt")

    # Attach labels to the grid
    grid.attach(label1, 0, 0, 1, 1)  # Row 0, column 0, width 1, height 1
    grid.attach(prompt, 1, 0, 1, 1)
    grid.attach(label2, 0, 1, 1, 1)
    grid.attach(neg_prompt, 1, 1, 1, 1)

    return grid

# Prompt save event
def handle_prompt_save(button):
    prompt = prompt_input.get_text()
    neg_prompt = neg_prompt_input.get_text()
    data = {
        "prompt": prompt,
        "neg_prompt": neg_prompt
    }
    with open('prompt.json', 'w') as jsonfile:
        data = json.dump(data, jsonfile)
    #print(f'Input: {prompt}')
    dialog = Gtk.MessageDialog(parent=None, type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, message_format="Prompt saved!")
    dialog.run()
    dialog.destroy()

window = Gtk.Window()
window.set_title("Overwrite Default Prompt")
window.connect("destroy", Gtk.main_quit)

# grid = create_table()
vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = SPACING)
window.add(vbox)

prompt_label = Gtk.Label(label="Prompt:")
prompt_label.set_halign(Gtk.Align.START)
vbox.add(prompt_label)
prompt_input = Gtk.Entry()
vbox.add(prompt_input)

neg_prompt_label = Gtk.Label(label="Negative Prompt:")
neg_prompt_label.set_halign(Gtk.Align.START)
vbox.add(neg_prompt_label)
neg_prompt_input = Gtk.Entry()
vbox.add(neg_prompt_input)

hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
vbox.add(hbox)

save_button = Gtk.Button(label="Save")
save_button.set_margin_top(8)
save_button.set_hexpand(False)
save_button.connect("clicked", handle_prompt_save)
hbox.pack_end(save_button, False, False, 0)
hbox.add(save_button)

window.set_border_width(SPACING)
window.set_size_request(400, -1)
window.set_position(Gtk.WindowPosition.CENTER)
window.set_resizable(False)
pixbuf = GdkPixbuf.Pixbuf.new_from_file("/home/avijit/hello/icon.png")
window.set_icon(pixbuf)
window.show_all()
Gtk.main()

""" data = {
    "prompt": "a high quality apple",
    "neg_prompt": "low quality"
}

with open('prompt.json', 'w') as jsonfile:
    data = json.dump(data, jsonfile) """


