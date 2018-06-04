<template>
    <div class="article-view">
    abc
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
            this.$axios.get('/articledetail' , {id: this.$route.params.id})
            .then((response) => {
                if(response.status === 200) {
                    console.log(response)
                    this.articleInfo = response.data.data;
                }
            })
        }
    }
</script>
<style>

</style>