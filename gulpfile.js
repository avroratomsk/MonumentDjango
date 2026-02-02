import gulp from "gulp";
import { path, pathAdmin } from "./gulp/config/path.js";
import { plugins } from "./gulp/config/plugins.js";

global.app = {
  path: path,
  pathAdmin: pathAdmin,
  gulp: gulp,
  plugins: plugins
}

import { copy, copyAdmin } from "./gulp/tasks/copy.js";
import { reset, resetAdmin } from "./gulp/tasks/reset.js";
import { html, htmlAdmin } from "./gulp/tasks/html.js";
import { server } from "./gulp/tasks/server.js";
import { scss, scssAdmin } from "./gulp/tasks/scss.js";
import { js, jsAdmin } from "./gulp/tasks/js.js";
import { images, imagesAdmin } from "./gulp/tasks/images.js";
import { otfToTtf, ttfToWoff, fonstStyle } from "./gulp/tasks/fonts.js";
import { sprite, spriteAdmin } from "./gulp/tasks/sprite.js";

function watcher() {
  gulp.watch(path.watch.files, copy);
  gulp.watch(path.watch.html, html);
  gulp.watch(path.watch.scss, scss);
  gulp.watch(path.watch.js, js);
  gulp.watch(path.watch.images, images);

  gulp.watch(pathAdmin.watch.files, copyAdmin);
  gulp.watch(pathAdmin.watch.html, htmlAdmin);
  gulp.watch(pathAdmin.watch.scss, scssAdmin);
  gulp.watch(pathAdmin.watch.js, jsAdmin);
  gulp.watch(pathAdmin.watch.images, imagesAdmin);
}

export { sprite };

const fonts = gulp.series(otfToTtf, ttfToWoff, fonstStyle);

const mainTasks = gulp.series(fonts, gulp.parallel(copy, html, scss, js, images, sprite, copyAdmin, htmlAdmin, scssAdmin, jsAdmin, imagesAdmin, spriteAdmin));

const dev = gulp.series(reset, resetAdmin, mainTasks, gulp.parallel(watcher, server));
const build = gulp.series(reset, resetAdmin, mainTasks);

gulp.task('default', dev);
gulp.task('build', build);