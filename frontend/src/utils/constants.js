require("dotenv").config();

export const drawerWidth = 240;
export const url = process.env.NODE_ENV === "development" ? "http://localhost:" + process.env.REACT_APP_BACKEND_PORT : "https://slackr-unsw.herokuapp.com";

export const PERMISSION_IDS = {
  OWNER: 1,
  MEMBER: 2
};
export const PAGINATION_SIZE = 50;
export const SLICE_SIZE = 10;
