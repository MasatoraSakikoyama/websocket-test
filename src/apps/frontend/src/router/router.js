/* globals Vue */
import VueRouter from 'vue-router';
import chat from '../components/contents/chat/chat';
import login from '../components/contents/login/login';

Vue.use(VueRouter);

const routes = [
  { path: '/', name: 'home', component: chat },
  { path: '/login', name: 'login', component: login },
];

export default class AppRouter extends VueRouter {
  constructor() {
    super({
      history: true,
      saveScrollPosition: true,
      routes,
    });
  }
}
