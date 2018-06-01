import Vue from 'vue'
import Router from 'vue-router'
import Article from '@/pages/admin/article_write/article'
import Manage from '@/pages/admin/article_manage/manage'

Vue.use(Router)

export default new Router({
  routes: [
    {
        path: '/article',
        component: Article
    },
    {
        path: '/manage',
        component: Manage
    }
  ]
})
