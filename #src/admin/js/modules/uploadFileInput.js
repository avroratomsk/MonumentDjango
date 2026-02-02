// const inputFiles = document.querySelectorAll('.form__controls-file');
//
// const uploadFile  = (e) => {
//   const formImages = document.querySelector('.form-images');
//   const files = e.currentTarget.files;
//   for(let i=0; i < files.length; i++ ){
//     const file = files[i];
//     formImages.innerHTML += `<img src="/${file.name}" alt="${file.name}">`;
//   }
// }
//
// inputFiles[0].addEventListener("change", function(event) {
//   const files = event.target.files; // Получаем первый файл
//   for(let i=0; i < files.length; i++ ){
//     const file = files[i];
//     if (file) {
//       const reader = new FileReader(); // Создаем FileReader
//       reader.onload = function(e) {
//         // const preview = document.getElementById("imagePreview");
//         // preview.src = e.target.result;
//         // preview.style.display = "block";
//
//         const formImages = document.querySelector('.form-images');
//         formImages.innerHTML += `<img src="/${e.target.result}" alt="${file.name}">`;
//       };
//       reader.readAsDataURL(file);
//     }
//   }
//
// });
//
//
// // inputFiles?.forEach(file => file.addEventListener('change', uploadFile))