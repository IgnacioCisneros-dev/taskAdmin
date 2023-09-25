from fastapi import FastAPI
from routers import usuario_route, tarea_route

app = FastAPI(title='Administrador de tareas.',
              description='API que ayuda a la gestion y control de tareas.',
              version='0.0.1')

app.include_router(usuario_route.router_usuarios)
app.include_router(tarea_route.router_tareas)
