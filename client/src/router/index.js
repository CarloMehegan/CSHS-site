import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Classes from "../views/Classes.vue";
import Projects from "../views/Projects.vue";
import Create from "../views/Create.vue";
import Account from "../views/Account.vue";
import SignIn from "../views/SignIn.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/Classes",
    name: "Classes",
    component: Classes
  },
  {
    path: "/Projects",
    name: "Projects",
    component: Projects
  },
  {
    path: "/Create",
    name: "Create",
    component: Create
  },
  {
    path: "/Account",
    name: "Account",
    component: Account
  },
  {
    path: "/SignIn",
    name: "SignIn",
    component: SignIn
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
