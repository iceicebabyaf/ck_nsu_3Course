import os
import cv2
from lab_1.coins_contour_detection import counting_contours

def sorted_conturs(image_path, output_path, min_size, max_size):
    """
    Выполняет поиск и фильтрацию контуров на изображении, 
    отрисовывает только подходящие контуры и сохраняет результат.

    Parameters
    ----------
    image_path : str
        Путь к исходному изображению.
    output_path : str
        Путь для сохранения изображения с отрисованными контурами.
    min_size : int
        Минимальная площадь контура для фильтрации.
    max_size : int
        Максимальная площадь контура для фильтрации.

    Returns
    -------
    int
        Количество найденных объектов, площадь которых находится в пределах [min_size, max_size].
        Возвращает 0 в случае ошибки.
    """
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # img to grayscale
        img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if img_color is None:
            raise FileNotFoundError(f"Image not found: {image_path}")
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

        # list of contours
        contours = counting_contours(img_gray, 50, 150, 127, 255, min_size, max_size)

        # accepted contours
        cv2.drawContours(img_color, contours, -1, (0, 255, 0), 3)
        cv2.imwrite(output_path, img_color)

        return len(contours)

    except FileNotFoundError as e:
        print("File error:", e)
        return 0
    except cv2.error as e:
        print("OpenCV error:", e)
        return 0
    except Exception as e:
        print("Unexpected error:", e)
        return 0


if __name__ == "__main__":
    count = sorted_conturs("input_data/res.png", "output_data/image_1.png", 100, 5000)
    print("Objects count:", count)
