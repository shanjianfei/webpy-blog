<template>
    <div class="page-manage-article">
        <div class="article-info" v-for="item in articlesInfo">
            <div class="article-title">
                <p>{{item.title}}</p>
            </div>
            <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6 item-info-left" style="text-align: left">
                    <span>{{item.create_time}}</span>
                    <span class="glyphicon glyphicon-book" aria-hidden="true">100</span>
                    <span class="glyphicon glyphicon-comment" aria-hidden="true">20</span>
                </div>
                <div class="col-md-6 col-sm-6 col-xs-6" style="text-align: right">
                    <div class="row">
                        <div class="col-md-6 col-sm-6 col-xs-6 col-md-offset-6 col-sm-offset-6 col-xs-offset-6"
                                id="manage-operate">
                            <router-link :to="{name: 'Article', params: {id: item.article_id}}">
                                <span>查看</span>
                            </router-link>
                            <a @click="deleteArticle(item.article_id)">
                                <span>删除</span>
                            </a>
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
            deleteArticle: function(id) {
                this.$axios.delete('/article', {params:{id: id}})
                .then((response) => {
                    if(response.status === 200 && response.data.status === 'success') {
                        for(var i = 0; i < this.articlesInfo.length; i++) {
                            if(this.articlesInfo[i].article_id === id) {
                                this.articlesInfo.splice(i, 1);
                                alert('删除成功');
                                break;
                            }
                        }
                    }
                })
                .catch((error) => {
                    alert('删除失败');
                })
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
    .article-title p {
        color: #4f4f4f;
    }
    .article-info {
        border-bottom: 1px dotted #ddd;
    }

    .item-info-left span {
        margin-right: 1.5rem;
        color: #999;
    }

    #manage-operate span {
        padding: 0px .5rem;
        border-right: 1px solid #e9e9e9
    }

    #manage-operate {
        text-align: right;
    }

    #manage-operate a {
        text-decoration: none;
    }

    #manage-operate>a {
        cursor: pointer;
    }
</style>