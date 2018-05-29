<template>
    <div class="article-container">
        <articles></articles>
    </div>
</template>
<script>
    import articles from "@/pages/article/children/Article"
    export default {
        components: {
            articles,
        },
        watch: {
            '$route': function(to, from) {
                let id = to.params.id
                this.type = id
            }
        }
    }
</script>