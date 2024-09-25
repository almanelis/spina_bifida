import matplotlib.pyplot as plt


def visualize_distribution(df):
    # Подсчет количества элементов в каждом классе
    class_counts = df['class'].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar([0, 1], class_counts.values)
    ax.set_title('Изначальное распределение классов')
    ax.set_ylabel('Количество экземпляров')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Патологии нет', 'Патология есть'])

    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

    plt.show(fig)


def visualize_ba(df, balanced_dataset):
    df['Class'] = df['pathology']
    balanced_dataset['class'] = balanced_dataset['class']

    # Подсчет количества элементов в каждом классе до обработки
    class_counts_before = df['pathology'].value_counts()

    # Подсчет количества элементов в каждом классе после обработки
    class_counts_after = balanced_dataset['class'].value_counts()

    # Создание subplot
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    # Построение столбчатой диаграммы для исходного распределения
    bars1 = ax1.bar([0, 1], class_counts_before.values)
    ax1.set_ylabel('Количество экземпляров')
    ax1.set_title('Изначальное распределение классов')
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(['Патология есть', 'Патологии нет'])

    # Добавление количества экземпляров на столбцы
    for bar in bars1:
        height = bar.get_height()
        ax1.annotate('{}'.format(height),
                     xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')

    # Построение столбчатой диаграммы для распределения после обработки
    bars2 = ax2.bar([0, 1], class_counts_after.values)
    ax2.set_ylabel('Количество экземпляров')
    ax2.set_title('Распределение после обработки')
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(['Патология есть', 'Патологии нет'])

    # Добавление количества экземпляров на столбцы
    for bar in bars2:
        height = bar.get_height()
        ax2.annotate('{}'.format(height),
                     xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom')

    plt.tight_layout()
    plt.show()
