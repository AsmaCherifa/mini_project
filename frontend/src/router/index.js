import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import Home from '../views/HomeView.vue';


const routes = [
  { path: '/login', component: LoginView },
  { path: '/', component: Home },


];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
