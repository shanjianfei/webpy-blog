import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/index/login/Login'
import Home from '@/pages/index/home/Home'
import ArticleContainer from '@/pages/index/article/ArticleContainer'
import ArticleContent from '@/pages/index/article/children/ArticleContent'

Vue.use(Router)

export default new Router({
  routes: [
    {
        path: '/',
        redirect: '/home'
    },
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
                redirect: 'page/homepage'
            },
            {
                path: 'page/:id',
                component: ArticleContainer,
            },
            {
                path: 'articlecontent',
                component: ArticleContent
            },

        ]
    },
  ]
})
