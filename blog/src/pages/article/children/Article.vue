<template>
    <div class="article">
        <div v-for="item in info">
            <a>
                <div class="row"><span class="label label-primary">{{item.type}}</span></div>
                <div class="row">
                    <div class="col-md-8">
                        <h2>{{item.title}}</h2>
                        <div class="detail">
                            <span>{{item.datetime}}</span>
                            &nbsp;&nbsp;&nbsp;&nbsp;
                            <span>阅读量: {{item.clickRate}}</span>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <img src="/static/img/js.jpg">
                    </div>
                </div>
            </a>
        </div>
        
    </div>
</template>
<script>
    import {mapState} from 'vuex'
    export default {
        methods: {

        },
        computed: mapState({
            // 箭头函数可使代码更简练
            info: state => state.info,
        }),
        created: function() {
            console.log(this.$store.state.info)
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
    .article a {
        cursor: pointer;
    }
    .article>div {
        background: #2d2d2d;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .article img {
        width: 200px;
        height: 100px;
        margin-bottom: 20px;
    }
</style>