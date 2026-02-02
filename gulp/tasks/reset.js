import { deleteAsync } from "del";

export const reset = () => {
  return deleteAsync(app.path.clean)
}

export const resetAdmin = () => {
  return deleteAsync(app.pathAdmin.cleanAdmin)
}
