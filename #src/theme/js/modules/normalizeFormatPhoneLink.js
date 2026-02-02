/**
 * Складывает два числа и возвращает результат.
 *
 * @param {number} a - Первое число для сложения.
 * @param {number} b - Второе число для сложения.
 * @returns {number} Сумма двух чисел.
 * @example

*/

const regNum = document.querySelectorAll("[data-phone]");

if (regNum) {
  regNum.forEach(num => {
    let number = formatPhoneNumber(num.dataset.phone);
    num.href = `tel:${number}`;
  });
}

function formatPhoneNumber(phoneNumber) {

  // Убираем все лишние символы (скобки, пробелы, тире)
  let cleanedNumber = phoneNumber.replace("tel:", "").replace(/[\s\-\(\)]/g, "");

  // Если номер уже начинается на +7, ничего не делаем
  if (cleanedNumber.startsWith("+7")) {
    return cleanedNumber;
  }

  // Если номер начинается на 8, заменяем на +7
  if (cleanedNumber.startsWith("8")) {
    return "+7" + cleanedNumber.slice(1);
  }

  // В остальных случаях добавляем +7 к началу
  return "+7" + cleanedNumber;
}