export const server = (done) => {
  app.plugins.browsersync.init({
    proxy: '127.0.0.1:8000', // Адрес вашего Django-сервера
    notify: false, // Отключает уведомления
    open: true, // Автоматически открывает браузер
    port: 3000 // Порт, на котором BrowserSync будет работать
  });
}