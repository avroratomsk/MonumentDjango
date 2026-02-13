// Создание правильной ссылка номера телефона
const regNum = document.querySelectorAll("a[href^=\"tel:\"]");
if (regNum) {
  regNum.forEach(num => {
    let number = formatPhoneNumber(num.href);
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