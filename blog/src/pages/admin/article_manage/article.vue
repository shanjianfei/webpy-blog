<template>
    <div class="article-view">
        <h1 id="article-title-view">{{articleInfo.title}}</h1>
        <div class="text" id="article-content-view"><p>{{articleInfo.article}}</p></div>
    </div>
</template>
<script>
    export default {
        data: function () {
            return {
                articleInfo: {}
            }
        },
        mounted: function() {
            this.$axios.get('/articledetail' , {params: {id: this.$route.params.id}})
            .then((response) => {
                if(response.status === 200) {
                    this.articleInfo = response.data.data[0];
                }
            })
        }
    }
</script>
<style>
    .article-view {
        text-align: left;
    }
</style>