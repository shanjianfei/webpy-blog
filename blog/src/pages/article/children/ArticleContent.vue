<template>
    <div class="article-content">
        <h1>{{title}}</h1>
        <div class="text"><p>{{content}}</p></div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                title: '',
                content: ''
            }
        },
        mounted: function() {
            this.title = 'vue 前端登录拦截',
            this.content = "dddd&n bsp;ddddd ddddd dddddddddd d&#10;dd dddd dddddddddd dd dddddggdd dd&nbsp;dd dddddddddd dddd ddddd&#10;dddddddddd ddddddd ddddd dggg ggggg gg ggg gggggggg gggeeee eeeeeeet ttttt tttt\r\naa"
        }
    }
</script>
<style>
    .text {
        text-align: left;
    }
</style>