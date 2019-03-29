;(function (f) {
    $.extend(window,{
        tool: f(),
    })
}(function () {
    let pagination = function (id, options) {
        console.log(id, options);
        return new pagination.fn.init(id, options);
    };
    pagination.defaults = {
        pageNumber    : 0,
        pageSize      : 0,
        isFirst       : false,
        isLast        : false,
        totalElements : 0,
        totalPages    : 0,
        hasNext       : false,
        hasPrevious   : false,
    };
    pagination.prototype    = pagination.fn = {
        init : function (id, options) {
            let pageInfo = this.pageInfo = $("#" + id);

            let settings = this.settings = $.extend(true, pagination.defaults, options);

            let first     = settings.isFirst?"disabled":"";
            let previous  = settings.hasPrevious?"":"disabled";
            let last     = settings.isLast?"disabled":"";
            let next  = settings.hasNext?"":"disabled";
            let firstHref     = settings.isFirst?"javascript:void(0);":"?pageNum=0&pageSize="+settings.pageSize;
            let previousHref  = settings.hasPrevious?"?pageNum="+(settings.pageNumber-1)+"&pageSize="+settings.pageSize:"javascript:void(0);";
            let lastHref     = settings.isLast?"javascript:void(0);":"?pageNum="+(settings.totalPages-1);
            let nextHref  = settings.hasNext?"?pageNum="+(settings.pageNumber+1)+"&pageSize="+settings.pageSize:"javascript:void(0);";


            let appendPageFrontElements = [
                '<li class="footable-page-arrow '+first+'">',
                    '<a data-page="first" href='+firstHref+'>«</a></li>',
                '<li class="footable-page-arrow '+previous+'">',
                    '<a data-page="prev" href='+previousHref+'>‹</a></li>',
            ].join('\n');
            pageInfo.append(appendPageFrontElements);
            // 生成三页
            let pages = [];
            // 生成前页码
            if(settings.hasPrevious){
                pages.push('<li class="footable-page"><a data-page="" href="?pageNum='+(settings.pageNumber-1)+'&pageSize='+settings.pageSize+'">'+settings.pageNumber+'</a></li>');
            }
            //生成当前页码
            pages.push('<li class="footable-page active"><a data-page="" href="javascript:void(0);">'+(settings.pageNumber+1)+'</a></li>');
            //生成后页码
            if(settings.hasNext){
                pages.push('<li class="footable-page"><a data-page="" href="?pageNum='+(settings.pageNumber+1)+'&pageSize='+settings.pageSize+'">'+(settings.pageNumber+2)+'</a></li>');
            }
            pageInfo.append(pages);
            let appendPageBehandElements = [
                '<li class="footable-page-arrow '+next+'">',
                    '<a data-page="next" href='+nextHref+'>›</a></li>',
                '<li class="footable-page-arrow '+last+'">',
                    '<a data-page="last" href='+lastHref+'>»</a></li>',
                '<li class="footable-page-arrow">',
                '<a href="javascript:void(0);">',
                    settings.pageNumber + 1 + '/' + settings.totalPages,
                '</a>',
                '</li>',
            ].join("\n");

            pageInfo.append(appendPageBehandElements);
            return pagination; // 重要
        },
        know : function () {
            console.log("不知道怎么用")
        },
    };
    pagination.fn.init.prototype = pagination.fn;

    return pagination;


}));