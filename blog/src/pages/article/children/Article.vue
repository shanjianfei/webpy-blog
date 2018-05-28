<template>
    <div class="article">
        <a>
            <div class="row"><span class="label label-primary">js</span></div>
            <div class="row">
                <div class="col-md-8">
                    <h2>{{title}}</h2>
                    <div class="detail">
                        <span>{{datetime}}</span>
                        &nbsp;&nbsp;&nbsp;&nbsp;
                        <span>阅读量: {{clickRate}}</span>
                    </div>
                </div>
                <div class="col-md-4">
                    <img src="/static/img/js.jpg">
                </div>
            </div>
        </a>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                title: 'vue 前端登录拦截',
                datetime: '2018-05-28 16:58:03',
                clickRate: 0
            }
        }
    }
</script>
<style>
    .article {
        margin: 10px;
    }
    .article .row {
        margin-left: 0;
        margin-right: 0;
        text-align: left;
    }
    .article .detail {
        margin-top: 20px;
    }
    a {
        cursor: pointer;
    }
    .article img {
        width: 200px;
        height: 100px;
        margin-bottom: 20px;
    }
</style>