import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return

    # Create 800x600 window
    window = glfw.create_window(800, 600, "HCI CG Lab 1 - Custom Clear Color", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Print OpenGL version & renderer
    version = glGetString(GL_VERSION).decode('utf-8')
    renderer = glGetString(GL_RENDERER).decode('utf-8')
    print(f"GL Version: {version}")
    print(f"GL Renderer: {renderer}")

    # Main render loop
    while not glfw.window_should_close(window):
        # Custom clear color: Dark Teal
        glClearColor(0.1, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
