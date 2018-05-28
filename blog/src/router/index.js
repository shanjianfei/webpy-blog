import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/login/Login'
import Home from '@/pages/home/Home'
import ArticleContainer from '@/pages/article/ArticleContainer'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
        path: '/home',
        component: Home,
        children: [
            {
                path: '',
                component: ArticleContainer
            }
        ]
    },
  ]
})
