<template>
    <div class="page-manage-article">
        <div class="article-info" v-for="item in articlesInfo">
            <div class="article-title" @click="viewAticle">{{item.title}}</div>
            <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6" style="text-align: left">{{item.create_time}}</div>
                <div class="col-md-6 col-sm-6 col-xs-6" style="text-align: right">
                    <div class="row">
                        <div class="col-md-6 col-sm-6 col-xs-6 col-md-offset-6 col-sm-offset-6 col-xs-offset-6"
                                id="manage-operate">
                            <a>查看</a>
                            <a>删除</a>
                        </div>
                    </div>
                </div>
            </div>
            <br/>
        </div>
    </div>
</template>
<script>
    export default({
        data() {
            return {
                articlesInfo: [],
            }
        },
        methods: {
            viewAticle: function() {

            }
        },
        mounted: function() {
            this.$axios.get('/article')
            .then((response) => {
                if(response.status === 200) {
                    this.articlesInfo = response.data.data;
                }
            })
        }
    })
</script>
<style>
    .article-title {
        text-align: left;
        font-size: 18px;
        margin-top: 45px;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .article-info {
        border-bottom: 1px dotted #ddd;
    }
    #manage-operate {
        text-align: right;
    }

    #manage-operate>a {
        cursor: pointer;
    }
</style>