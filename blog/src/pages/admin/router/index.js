import Vue from 'vue'
import Router from 'vue-router'
import ArticleWrite from '@/pages/admin/article_write/article'
import Manage from '@/pages/admin/article_manage/manage'
import Article from '@/pages/admin/article_manage/article'

Vue.use(Router)

export default new Router({
  routes: [
    {
        path: '/articlewrite',
        component: ArticleWrite
    },
    {
        path: '/manage',
        component: Manage
    },
    {
        path: '/article/:id',
        component: Article,
        // props: true
    }
  ]
})
