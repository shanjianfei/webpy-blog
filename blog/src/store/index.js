import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {info:
        [
            {
                type: 'js',
                title: 'vue 前端登录拦截',
                datetime: '2018-05-28 23:10:10',
                clickRate: 0
            },
            {
                type: 'python',
                title: 'python 单例模式',
                datetime: '2018-05-28 23:10:10',
                clickRate: 0
            },
            {
            	type: 'web',
            	title: 'webpy简介',
            	datetime: '2018-05-28 23:10:10',
                clickRate: 0
            },
            {
            	type: 'html',
            	title: '父元素高度为0',
            	datetime: '2018-05-28 23:10:10',
                clickRate: 0
            },
            {
            	type: 'css',
            	title: '如何去除a标签的下划线',
            	datetime: '2018-05-28 23:10:10',
                clickRate: 0
            },
        ]
    }
})

export default store