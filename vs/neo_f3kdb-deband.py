import vapoursynth as vs
core = vs.get_core()

core.neo_f3kdb.Deband(video_in, range=15, y=64, cb=64, cr=64, grainy=64, grainc=0, dynamic_grain=True, sample_mode=2).set_output()