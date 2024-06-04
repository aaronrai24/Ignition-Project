def aggregateFunct(qval, interpolated, finished, blockContext, queryContext):
    cnt = blockContext.getOrDefault('cnt',0)
    if qval.quality.isGood():
        blockContext['cnt']=int(cnt)+1
     
    if finished:
        return blockContext.getOrDefault('cnt', 0)