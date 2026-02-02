import * as nodePath from 'path';
const rootFolder = nodePath.basename(nodePath.resolve())

const buildFolder = `./main/core/theme`;
const srcFolder = `./#src/theme`;

const buildFolderAdmin = `./main/core/admin`;
const srcFolderAdmin = `./#src/admin`;

export const path = {
  build: {
    js: `${buildFolder}/js/`,
    css: `${buildFolder}/css/`,
    html: `${buildFolder}/`,
    images: `${buildFolder}/img/`,
    fonts: `${buildFolder}/fonts/`,
    files: `${buildFolder}/files/`,
    deploy: `${buildFolder}/**/*`,
  },
  src: {
    js: `${srcFolder}/js/app.js`,
    scss: `${srcFolder}/scss/style.scss`,
    html: `${srcFolder}/**/*.html`,
    images: `${srcFolder}/img/**/*.{jpg,jpeg,png,gif,webp}`,
    svg: `${srcFolder}/img/**/*.svg`,
    files: `${srcFolder}/files/**/*.*`,
    svgicons: `${srcFolder}/svgicons/*.svg`,
  },
  watch: {
    js: `${srcFolder}/js/**/*.js`,
    scss: `${srcFolder}/scss/**/*.scss`,
    html: `${srcFolder}/**/*.html`,
    images: `${srcFolder}/img/**/*.{jpg,jpeg,png,svg,gif,ico,webp}`,
    files: `${srcFolder}/files/**/*.*`,
  },
  clean: buildFolder,
  buildFolder: buildFolder,
  srcFolder: srcFolder,
  rootFolder: rootFolder,
  ftp: ``
}

export const pathAdmin = {
  build: {
    js: `${buildFolderAdmin}/js/`,
    css: `${buildFolderAdmin}/css/`,
    html: `${buildFolderAdmin}/`,
    images: `${buildFolderAdmin}/img/`,
    fonts: `${buildFolderAdmin}/fonts/`,
    files: `${buildFolderAdmin}/files/`,
    deploy: `${buildFolderAdmin}/**/*`,
  },
  src: {
    js: `${srcFolderAdmin}/js/app.js`,
    scss: `${srcFolderAdmin}/scss/style.scss`,
    html: `${srcFolderAdmin}/**/*.html`,
    images: `${srcFolderAdmin}/img/**/*.{jpg,jpeg,png,gif,webp}`,
    svg: `${srcFolderAdmin}/img/**/*.svg`,
    files: `${srcFolderAdmin}/files/**/*.*`,
    svgicons: `${srcFolderAdmin}/svgicons/*.svg`,
  },
  watch: {
    js: `${srcFolderAdmin}/js/**/*.js`,
    scss: `${srcFolderAdmin}/scss/**/*.scss`,
    html: `${srcFolderAdmin}/**/*.html`,
    images: `${srcFolderAdmin}/img/**/*.{jpg,jpeg,png,svg,gif,ico,webp}`,
    files: `${srcFolderAdmin}/files/**/*.*`,
  },
  cleanAdmin: buildFolderAdmin,
  buildFolderAdmin: buildFolderAdmin,
  srcFolderAdmin: srcFolderAdmin,
  rootFolder: rootFolder,
  ftp: ``
}