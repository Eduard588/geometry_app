# task1_point_projections.py
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

# Настройка страницы
st.set_page_config(layout="wide")
st.title("🎯 Начертательная геометрия: Задача 1 — Проекции точки")

# Генерация новой задачи
if "A" not in st.session_state:
    st.session_state.A = np.random.randint(20, 60, size=3)  # x, y, z
    st.session_state.task_type = np.random.choice([
        {"desc": "на 10 мм ближе и на 15 мм выше", "dx": 0, "dy": -10, "dz": 15},
        {"desc": "на 20 мм дальше и на 10 мм ниже", "dx": 0, "dy": 10, "dz": -10},
        {"desc": "на 15 мм правее и на 5 мм выше", "dx": 15, "dy": 0, "dz": 5},
    ])

A = st.session_state.A
x, y, z = A
task = st.session_state.task_type

# Правильные координаты точки B
B_true = (x + task["dx"], y + task["dy"], z + task["dz"])
Bx_true, By_true, Bz_true = B_true

# Интерфейс
st.write("### 📝 Условие задачи:")
st.write(f"Дана точка A({int(x)}, {int(y)}, {int(z)}).")
st.write("1. Постройте её проекции:")
st.write("   - **A₁** — горизонтальная проекция (на П1)")
st.write("   - **A₂** — фронтальная проекция (на П2)")
st.write("   - **A₃** — профильная проекция (на П3)")
st.write(f"2. Постройте точку B, которая {task['desc']} точки A.")

# Поля ввода
st.write("### ✏️ Введите координаты проекций точки A:")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**A₁ (x, y)**")
    Ax1 = st.number_input("A₁_x", min_value=0, max_value=100, value=0, key="a1x")
    Ay1 = st.number_input("A₁_y", min_value=0, max_value=100, value=0, key="a1y")

with col2:
    st.write("**A₂ (x, z)**")
    Ax2 = st.number_input("A₂_x", min_value=0, max_value=100, value=0, key="a2x")
    Az2 = st.number_input("A₂_z", min_value=0, max_value=100, value=0, key="a2z")

with col3:
    st.write("**A₃ (y, z)**")
    Ay3 = st.number_input("A₃_y", min_value=0, max_value=100, value=0, key="a3y")
    Az3 = st.number_input("A₃_z", min_value=0, max_value=100, value=0, key="a3z")

st.write("### ✏️ Введите координаты точки B:")
colB1, colB2, colB3 = st.columns(3)
with colB1:
    Bx = st.number_input("B_x", min_value=0, max_value=100, value=0, key="bx")
with colB2:
    By = st.number_input("B_y", min_value=0, max_value=100, value=0, key="by")
with colB3:
    Bz = st.number_input("B_z", min_value=0, max_value=100, value=0, key="bz")

# Кнопки
check_col, new_col = st.columns([1, 1])
with check_col:
    check = st.button("✅ Проверить")
with new_col:
    if st.button("🔄 Новая задача"):
        st.session_state.pop("A")
        st.rerun()

# Проверка и визуализация
if check:
    correct = True
    results = []

    # Проверка A₁
    if (Ax1, Ay1) == (x, y):
        results.append("A₁: ✅")
    else:
        results.append(f"A₁: ❌ (правильно: A₁({int(x)}, {int(y)}))")
        correct = False

    # Проверка A₂
    if (Ax2, Az2) == (x, z):
        results.append("A₂: ✅")
    else:
        results.append(f"A₂: ❌ (правильно: A₂({int(x)}, {int(z)}))")
        correct = False

    # Проверка A₃
    if (Ay3, Az3) == (y, z):
        results.append("A₃: ✅")
    else:
        results.append(f"A₃: ❌ (правильно: A₃({int(y)}, {int(z)}))")
        correct = False

    # Проверка B
    if (Bx, By, Bz) == B_true:
        results.append("B: ✅")
    else:
        results.append(f"B: ❌ (правильно: B({int(Bx_true)}, {int(By_true)}, {int(Bz_true)}))")
        correct = False

    # Вывод результата
    if correct:
        st.success("🎉 Отлично! Все ответы верны.")
    else:
        for res in results:
            st.error(res)

    # === 2D Чертёж ===
    st.write("### 📐 2D-чертёж проекций (стандартное расположение)")
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    axs = axs.flatten()

    # П2 — фронтальная (слева, сверху): A₂ и B₂
    axs[0].scatter(x, z, c='blue', s=60)
    axs[0].text(x + 2, z, "A₂", fontsize=12, color='blue', weight='bold')
    axs[0].scatter(Bx_true, Bz_true, c='purple', s=60)
    axs[0].text(Bx_true + 2, Bz_true, "B₂", fontsize=12, color='purple', weight='bold')
    axs[0].set_xlim(0, 80)
    axs[0].set_ylim(0, 80)
    axs[0].grid(True, linestyle='--', alpha=0.6)
    axs[0].set_title("П2: Фронтальная проекция")
    axs[0].set_xlabel("X")
    axs[0].set_ylabel("Z")

    # П3 — профильная (справа, сверху): A₃ и B₃
    axs[1].scatter(y, z, c='green', s=60)
    axs[1].text(y + 2, z, "A₃", fontsize=12, color='green', weight='bold')
    axs[1].scatter(By_true, Bz_true, c='purple', s=60)
    axs[1].text(By_true + 2, Bz_true, "B₃", fontsize=12, color='purple', weight='bold')
    axs[1].set_xlim(0, 80)
    axs[1].set_ylim(0, 80)
    axs[1].grid(True, linestyle='--', alpha=0.6)
    axs[1].set_title("П3: Профильная проекция")
    axs[1].set_xlabel("Y")
    axs[1].set_ylabel("Z")

    # П1 — горизонтальная (слева, снизу): A₁ и B₁
    axs[2].scatter(x, y, c='red', s=60)
    axs[2].text(x + 2, y, "A₁", fontsize=12, color='red', weight='bold')
    axs[2].scatter(Bx_true, By_true, c='purple', s=60)
    axs[2].text(Bx_true + 2, By_true, "B₁", fontsize=12, color='purple', weight='bold')
    axs[2].set_xlim(0, 80)
    axs[2].set_ylim(0, 80)
    axs[2].invert_yaxis()  # Ось Y направлена вниз
    axs[2].grid(True, linestyle='--', alpha=0.6)
    axs[2].set_title("П1: Горизонтальная проекция")
    axs[2].set_xlabel("X")
    axs[2].set_ylabel("Y")

    # Удаляем пустую ячейку
    fig.delaxes(axs[3])

    plt.tight_layout()
    st.pyplot(fig)

    # === 3D Визуализация ===
    st.write("### 🧊 3D-модель")
    fig_3d = go.Figure()

    # Точка A
    fig_3d.add_trace(go.Scatter3d(
        x=[x], y=[y], z=[z],
        mode='markers+text',
        text=["A"],
        textposition="top center",
        marker=dict(size=8, color='red'),
        name="A"
    ))

    # Проекции A
    fig_3d.add_trace(go.Scatter3d(
        x=[x], y=[y], z=[0],
        mode='markers+text',
        text=["A₁"],
        textposition="middle left",
        marker=dict(size=6, color='orange'),
        name="A₁"
    ))
    fig_3d.add_trace(go.Scatter3d(
        x=[x], y=[0], z=[z],
        mode='markers+text',
        text=["A₂"],
        textposition="top center",
        marker=dict(size=6, color='blue'),
        name="A₂"
    ))
    fig_3d.add_trace(go.Scatter3d(
        x=[0], y=[y], z=[z],
        mode='markers+text',
        text=["A₃"],
        textposition="top right",
        marker=dict(size=6, color='green'),
        name="A₃"
    ))

    # Точка B
    fig_3d.add_trace(go.Scatter3d(
        x=[Bx_true], y=[By_true], z=[Bz_true],
        mode='markers+text',
        text=["B"],
        textposition="top center",
        marker=dict(size=8, color='purple'),
        name="B"
    ))

    # Проекции B
    fig_3d.add_trace(go.Scatter3d(
        x=[Bx_true], y=[By_true], z=[0],
        mode='markers+text',
        text=["B₁"],
        textposition="middle right",
        marker=dict(size=6, color='magenta'),
        name="B₁"
    ))
    fig_3d.add_trace(go.Scatter3d(
        x=[Bx_true], y=[0], z=[Bz_true],
        mode='markers+text',
        text=["B₂"],
        textposition="bottom center",
        marker=dict(size=6, color='magenta'),
        name="B₂"
    ))
    fig_3d.add_trace(go.Scatter3d(
        x=[0], y=[By_true], z=[Bz_true],
        mode='markers+text',
        text=["B₃"],
        textposition="top left",
        marker=dict(size=6, color='magenta'),
        name="B₃"
    ))

    # Настройки 3D-сцены
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(title="X", range=[0, 80]),
            yaxis=dict(title="Y", range=[0, 80]),
            zaxis=dict(title="Z", range=[0, 80]),
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        margin=dict(l=0, r=0, b=0, t=50),
        title="3D-модель: точки A и B, их проекции"
    )

    st.plotly_chart(fig_3d, use_container_width=True)